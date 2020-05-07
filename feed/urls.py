from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, PostDownloadPDF\
    , PostLike#, CommentListView
from . import views
from .models import Comment


urlpatterns = [
    path('', PostListView.as_view(), name='feed-home'),
    path('feed/<int:pk>/', PostDetailView.as_view(), name='feed-detail'),   #works
    path('feed/<int:pk>/delete/', PostDeleteView.as_view(), name='feed-delete'),
    path('feed/<int:pk>/download/', PostDownloadPDF.as_view(), name='feed-download'),
    path('new/', PostCreateView.as_view(), name='feed-create'),

    path('feed/<int:pk>/like/', PostLike.as_view(), name='feed-like'),
    #path('comment/<int:id>/', CommentListView.as_view(), name='feed-post-comment'),   #works

    path('profile/<int:pk>/', views.view_profile, name='view-profile'),
    path('friends/', views.friends, name='feed-friends'),

    #friend/unfriend
    path('follow/<str:operation>/<int:pk>', views.updateFriendsList, name='update-friends'),

]

#<app>/<model>_<viewtype>.html naming convention

