from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'username' : 'ncumbo',
        'post_content' : 'This corona virus thing is dumb',
        'date' : '4/7/2020'
    },
    {
        'username': 'ncumbo',
        'post_content': 'Lets time travel with this post',
        'date': '4/8/2020'
    }
]

# Create your home feed page
def home(request):
    context = {
        'posts': posts
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
