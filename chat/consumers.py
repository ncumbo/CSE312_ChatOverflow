import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from channels.layers import get_channel_layer

from .models import Message, Room

class ChatConsumer(WebsocketConsumer):
    # get old messages
    def fetch_messages(self, data):
        print('fetch')
        messages = Message.last_20_messages()
        print(messages.values())
        fetch_seen = True       #turn all messages seen values = to true
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages, fetch_seen)
        }
        self.send_message(content)

    def send_message(self, message):    # Parse in content then straight away send message
        self.send(text_data=json.dumps(message))

    # create new messages
    def new_message(self, data):
        print('new message')
        author = data['from']   #from User loggedin
        author_user = User.objects.filter(username=author)[0]
        new_message_seen = False
        message = Message.objects.create(
            author=author_user,
            content=data['message'],
            seen=False,     #new
        )
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message, new_message_seen),
        }
        return self.send_chat_message(content)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)( #old
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):  # Receive message from event then sending it
        message = event['message']
        self.send(text_data=json.dumps(message))    # Send message to WebSocket

    #parse message to json
    def messages_to_json(self, messages, fetch_seen):
        result = []
        for mess in messages:
            result.append(self.message_to_json(mess, fetch_seen))
        return result

    def message_to_json(self, message, seen):     #json message from model
        return {
            'id': message.id,
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp),
            'seen': seen    #new
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)


