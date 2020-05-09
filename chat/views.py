from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json

from feed.models import Friend
from .models import Message
from django.contrib.auth.models import User


def index(request):      #messages = index
    try:
        friend = Friend.objects.get(currentUser=request.user)
        context = {
            'friends': friend.users.all(),
        }
    except Friend.DoesNotExist:
        context = {
            'friends': None,
        }

    return render(request, 'chat/index.html', context)

@login_required
def room(request, room_name):
    #Message

    context = {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    return render(request, 'chat/room.html', context)

    # return render(request, 'chat/room.html', {
    #     'room_name': mark_safe(json.dumps(room_name)),
    #     'username': mark_safe(json.dumps(request.user.username)),
    # })