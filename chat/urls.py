from django.urls import path

from .views import messages

app_name = 'chat'

urlpatterns = [
    path('messages/', messages, name='messages'),
]