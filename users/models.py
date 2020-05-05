from django.db import models
from django.contrib.auth.models import User
from django import forms


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.CharField(max_length=300, default="Change current Bio")
    image = models.ImageField(default='default_image.jpg', upload_to='profile_photos')

    def __str__(self):
        return f'{self.user.username} Profile'