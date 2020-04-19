from django import forms
from .models import Post

class Upload():

    image = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = ('content', 'image')