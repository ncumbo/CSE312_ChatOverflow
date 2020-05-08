from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)  #auto_now_add=True

    def __str__(self):
        return self.author.username

    def last_20_messages():
        return Message.objects.order_by('-timestamp').all()[:20]