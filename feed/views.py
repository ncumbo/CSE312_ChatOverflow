from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Post

# Create your home feed page
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)

def profile(request):
    return render(request, 'feed/profile.html', {'username': 'ncumbo'})

def login(request):
    return render(request, 'feed/login.html')

def friends(request):
    return render(request, 'feed/friends.html')

def messages(request):
    return render(request, 'feed/messages.html', {'username': 'ncumbo'})

def post_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            content = form.cleaned_data.get('content')
            messages.success(request, f'Post Submitted')
            return redirect('feed-home')
    else:
        form = UserCreationForm()
    return render(request, 'feed/post_form.html', {'form': form})

#Works
class PostListView(ListView):
    model = Post     #tells listviewto query a post
    template_name = 'feed/feed.html'    #template w naming convention <app>/<model>_<viewtype>.html naming convention
    context_object_name = 'posts'
    ordering = ['-date_posted'] #chronological ordering

class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.username = self.request.user    #set author to current signed in user
        return super().form_valid(form)

#delete a post
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

