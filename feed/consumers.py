from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
import json
from .models import Post

#class FeedConsumer(WebsocketConsumer):
    # def connect(self):
    #     self.room_name = self.scope['url_route']['kwargs']['game_id']
    #     self.room_group_name = f'Game_{self.room_name}'
    #     if self.scope['user'] == AnonymousUser():
    #         raise DenyConnection("Invalid User")

    #     self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )
    #     # If invalid game id then deny the connection.
    #     try:
    #         self.game = Game.objects.get(pk=self.room_name)
    #     except ObjectDoesNotExist:
    #         raise DenyConnection("Invalid Game Id")
    #     self.accept()

    # def receive(self, post_data):
    #     game_city = json.loads(post_data).get('game_city')
    #     self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'live_score',
    #             'game_id': self.room_name,
    #             'game_city': game_city
    #         }
    #     )

    # def disconnect(self, close_code):
    #     # Leave room group
    #     async_to_sync(self.channel_layer.group_discard)(
    #         self.room_group_name,
    #         self.channel_name
    #     )