from django import forms
from .models import Post, Comment

# class Upload(forms.ModelForm):
#
#     image = forms.FileField(required=False)
#
#     class Meta:
#         model = Post
#         fields = ('content', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)