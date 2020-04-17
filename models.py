from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	image = models.ImageField(default='default_image.jpg', upload_to='profile_photos')
	bio = models.TextField(max_length=280)

	def __str__(self):
		return f'{self.user.username} Profile'