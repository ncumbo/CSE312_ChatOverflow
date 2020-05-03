from django.conf.urls import re_path, url
from . import consumers

#routes to consumer. listens to websockets on consumers.py
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),   #use re_path bc URLRouter
    #url(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]