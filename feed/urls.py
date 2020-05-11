from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostDownloadPDF

from . import views
from .models import Comment


urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('feed/<int:pk>/', PostDetailView.as_view(), name='feed-detail'),
    path('feed/<int:pk>/delete/', PostDeleteView.as_view(), name='feed-delete'),
    path('feed/<int:pk>/download/', PostDownloadPDF.as_view(), name='feed-download'),
    path('new/', PostCreateView.as_view(), name='feed-create'),

    path('profile/<int:pk>/', views.view_profile, name='view-profile'),

    # friend/unfriend
    path('friends/', views.friends, name='feed-friends'),
    path('follow/<str:operation>/<int:pk>', views.updateFriendsList, name='update-friends'),

    # comment
    path('feed/<int:pk>/create_comment/', views.create_comment, name='create-comment'),

    # like
    path('likes/', views.like_post, name='like_post'),
]

#<app>/<model>_<viewtype>.html naming convention

