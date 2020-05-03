from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

from chat.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls')),    #matches what it has, then sends remaining pattern to feed.url
    path('register/', user_views.registerView, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    #chatrooms
    path('messages/', index, name='index'),
    path('chat/', include('chat.urls', namespace='chat')),
    #path('chat/', include('chat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)