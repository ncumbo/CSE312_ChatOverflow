from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostDownloadPDF
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('feed/<int:pk>/', PostDetailView.as_view(), name='feed-detail'),   #works
    path('feed/<int:pk>/delete/', PostDeleteView.as_view(), name='feed-delete'),
    path('feed/<int:pk>/download/', PostDownloadPDF.as_view(), name='feed-download'),
    path('new/', PostCreateView.as_view(), name='feed-create'),
    path('create/', PostCreateView.as_view(), name='feed-cre'),

    path('friends/', views.friends, name='feed-friends'),
    path('messages/', views.messages, name='feed-messages')
]

#<app>/<model>_<viewtype>.html naming convention