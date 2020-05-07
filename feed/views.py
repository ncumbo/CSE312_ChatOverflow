#P2
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, RedirectView, TemplateView
from django_xhtml2pdf.views import PdfMixin
from .models import Post, Comment
from .forms import CommentForm

#P3
from django.contrib.auth.models import User

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
        print(context['users'])
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        print(kwargs)
        print(self.kwargs.get('pk'))
        print(Comment.objects.filter(post_id=self.kwargs.get('pk')))

        context['comments'] = Comment.objects.filter(post_id=self.kwargs.get('pk'))
        return context

class PostDownloadPDF(PdfMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'image']

    success_url = '/'

    def form_valid(self, form): #overriding createView to add author before form submitted
        form.instance.username = self.request.user    #set author to current signed in user
        return super().form_valid(form) 

    #something here for ajax


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

class PostLike(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Post, slug=slug)
        url = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            obj.likes.add(user)
        return 1

def friends(request):
    return render(request, 'feed/friends.html', {'users': User.objects.all()})

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
        print(user)
    context = {'user': user}
    return render(request, 'users/profile.html', context)

def messages(request):
    return render(request, 'feed/messages.html', {'username': 'ncumbo'})