import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Message

#User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    #asynchronous provide higher level of performance bc it doesnt create additional
    #threads when handling requests
    #async used to call asynchronous functions that perform i/o

    #old messages
    def fetch_messages(self, data):
        print('fetch')
        messages = Message.last_20_messages()
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    #creat new message
    def new_message(self, data):
        print('new message')
        author = data['from']   #from User loggedin
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(
            author=author_user,
            content=data['message']
        )
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message),
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for mess in messages:
            result.append(self.message_to_json(mess))
        return result

    def message_to_json(self, message):     #json message from model
        return {
            'id': message.id,
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp),
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
        # data['command'] will either return fetch_message or new_message
        # and then run either of the commands
        # calls corresponding function in the dictionary
        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Parse in content then straight away send message
    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # Receive message from event then sending it
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))    # Send message to WebSocket