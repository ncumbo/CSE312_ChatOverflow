from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):      #messages = index
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })