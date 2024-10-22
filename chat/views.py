from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json

from feed.models import Friend
from .models import Message
from django.contrib.auth.models import User


def index(request):      #messages = index
    last_message_seen = "index:", Message.objects.reverse()[0].seen
    print("last message type: ", last_message_seen)
    #seen?
    try:
        friend = Friend.objects.get(currentUser=request.user)
        context = {
            'friends': friend.users.all(),
            'last_message_seen': last_message_seen[1]
        }
    except Friend.DoesNotExist:
        context = {
            'friends': None,
        }

    return render(request, 'chat/index.html', context)

@login_required
def room(request, room_name):

    context = {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        #'seen': Message.objects.get('seen'),
    }
    return render(request, 'chat/messaging.html', context)

    # return render(request, 'chat/messaging.html', {
    #     'room_name': mark_safe(json.dumps(room_name)),
    #     'username': mark_safe(json.dumps(request.user.username)),
    # })