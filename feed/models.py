from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#model for everyone with accounts

class Post(models.Model):
    #fields for a post. what django database will hold
    content = models.TextField(max_length=280)  #sets 280 characters per post
    date_posted = models.DateTimeField(default=timezone.now)   #sets date/time when post is created
    username = models.ForeignKey(User, on_delete=models.CASCADE)      #related table is User. If user is deleted, delete posts as well

    image = models.FileField(default='default_image.jpg', upload_to='meme_photos')

    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    #comments = models.TextField(max_length=280)

    def __str__(self):  #dunder = double underscore
        return self.content

    def get_absolute_url(self):
        return reverse('feed-detail', kwargs={'pk': self.pk})

