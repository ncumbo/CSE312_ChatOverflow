from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='feed-home'),
    path('profile/', views.profile, name='feed-profile'),
    path('login/', views.login, name='feed-login'),
    path('friends/', views.friends, name='feed-friends'),
    path('messages/', views.messages, name='feed-messages')
]