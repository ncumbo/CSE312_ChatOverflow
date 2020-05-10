from django.conf.urls import re_path, url
from django.urls import path
from . import consumers

#routes to consumer. listens to websockets on consumers.py
websocket_urlpatterns = [
    #re_path(r'ws/(?P<post_number>\w+)/$', consumers.FeedConsumer),   #use re_path bc URLRouter
    #path("ws/<id:pk>", consumers.FeedConsumer, name="feed-ws"),
]