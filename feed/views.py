#P2
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django_xhtml2pdf.views import PdfMixin
from .models import Post, Comment, Friend
from .forms import CommentForm

#P3
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)

#Works
class PostListView(ListView):
    model = Post
    template_name = 'feed/feed.html'    #template w naming convention <app>/<model>_<viewtype>.html naming convention
    context_object_name = 'posts'
    ordering = ['-date_posted'] #chronological ordering

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data()
        context['users'] = User.objects.all()
        return context

class PostDownloadPDF(PdfMixin, DetailView):
    model = Post

class PostDetailForm(forms.Form):
    message = forms.CharField()

class PostDetailView(DetailView):
    model = Post
    fields = ['likes']              #new - tim
    total_likes = 'total_likes'     #new - tim

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        # print(kwargs)
        # print(self.kwargs.get('pk'))
        # print(Comment.objects.filter(post_id=self.kwargs.get('pk')))
        context['comments'] = Comment.objects.filter(post_id=self.kwargs.get('pk'))

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'image']

    success_url = '/'

    def form_valid(self, form): #overriding createView to add author before form submitted
        form.instance.username = self.request.user    #set author to current signed in user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

def friends(request):
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

    return render(request, 'feed/friends.html', context)



def updateFriendsList(request, operation, pk):
    newFriend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, newFriend)
    elif operation == 'remove':
        Friend.unfriend(request.user, newFriend)

    friend = Friend.objects.get(currentUser=request.user)
    excludeList = []
    excludeList.append(request.user.id)
    for each in friend.users.all():
        excludeList.append(each.id)


    context = {
        'users': User.objects.exclude(id__in=excludeList),
        'friends': friend.users.all(),
    }
    return render(request, 'feed/friends.html', context)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {'user': user}
    return render(request, 'users/view_profiles.html', context)

#comments
@login_required
def create_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment() #instantiate new comment
            comment.post_id = pk
            comment.user_id = request.user.id
            comment.content = form.cleaned_data['content']
            comment.date_posted = form.cleaned_data['date_posted']
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'feed/create_comment.html', context)

#likes
#@login_required
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context ={
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('feed/like_section.html', context, request=request)
        return JsonResponse({'form': html})