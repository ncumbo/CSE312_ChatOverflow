from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, RedirectView
from django_xhtml2pdf.views import PdfMixin
from .models import Post

from django import forms

from django.core.files.storage import FileSystemStorage
from .forms import Upload

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)

#Works
class PostListView(ListView):
    model = Post     #tells listviewto query a post
    template_name = 'feed/feed.html'    #template w naming convention <app>/<model>_<viewtype>.html naming convention
    context_object_name = 'posts'
    ordering = ['-date_posted'] #chronological ordering

class PostDetailView(DetailView):
    model = Post

class PostDownloadPDF(PdfMixin, DetailView):
    model = Post
    template_name = "feed/post_detail.html"

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
    return render(request, 'feed/friends.html')

def messages(request):
    return render(request, 'feed/messages.html', {'username': 'ncumbo'})
#
# def upload(request):
#     content = {}
#     if request.method == 'POST':
#         uploads = request.FILES['file']
#         file = FileSystemStorage()
#         name = file.save(uploads.name, uploads)
#         content['url'] = file.url(name)
#     return render(request, 'feed/feed2.html', content)
#