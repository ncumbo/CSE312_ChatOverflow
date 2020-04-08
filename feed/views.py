from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'username' : 'ncumbo',
        'content' : 'This corona virus thing is dumb',
        'date_posted' : '4/7/2020'
    },
    {
        'username': 'ncumbo',
        'content': 'Lets time travel with this post',
        'date_posted': '4/8/2020'
    }
]

# Create your home feed page
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)

def profile(request):
    return render(request, 'feed/profile.html', {'username': 'ncumbo'})

def login(request):
    return render(request, 'feed/login.html')

def friends(request):
    return render(request, 'feed/friends.html')

def messages(request):
    return render(request, 'feed/messages.html', {'username': 'ncumbo'})
