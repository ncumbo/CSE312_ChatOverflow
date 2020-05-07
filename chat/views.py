from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json

from feed.models import Friend
from django.contrib.auth.models import User


def index(request):      #messages = index
    try:
        friend = Friend.objects.get(currentUser=request.user)
        excludeList = []
        excludeList.append(request.user.id)
        for each in friend.users.all():
            excludeList.append(each.id)

        context = {
            'users': User.objects.exclude(id__in=excludeList),
            'friends': friend.users.all(),
        }
    except Friend.DoesNotExist:
        excludeList = []
        excludeList.append(request.user.id)
        context = {
            'users': User.objects.exclude(id__in=excludeList),
            'friends': None,
        }

    return render(request, 'chat/index.html', context)

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })