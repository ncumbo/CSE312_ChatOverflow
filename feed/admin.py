from django.contrib import admin
from .models import Post, Comment, Friend

# Register your models here to show up on admin page
admin.site.register(Comment)
admin.site.register(Friend)
