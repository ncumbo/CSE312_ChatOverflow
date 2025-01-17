from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Room(models.Model):
    room_name = models.TextField()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)  #auto_now_add=True

    seen = models.BooleanField(default=True)
    #recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.author.username

    def last_20_messages():
        return Message.objects.order_by('timestamp').all()[:20]

