from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('feed/<int:pk>/', PostDetailView.as_view(), name='feed-detail'),   #works
    path('new/', PostCreateView.as_view(), name='feed-create'),
    path('feed/<int:pk>/delete/', PostDeleteView.as_view(), name='feed-delete'),

    path('profile/', views.profile, name='feed-profile'),
    path('login/', views.login, name='feed-login'),
    path('friends/', views.friends, name='feed-friends'),
    path('messages/', views.messages, name='feed-messages')
]

#<app>/<model>_<viewtype>.html naming convention