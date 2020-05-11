import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string

#def post_form(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save()    #save to database
#            username = form.cleaned_data.get('username')
#            content = form.cleaned_data.get('content')
#            messages.success(request, f'Post Submitted')
#            return redirect('feed-home')
#    else:
#        form = UserCreationForm()
#    return render(request, 'feed/post_form.html', {'form': form})

# Create your home feed page - good
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
    fields = ['likes']
    total_likes = 'total_likes'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(PostDetailView, self).get_context_data(*args, **kwargs)
    #     context['total_likes'] = Post.
    #     print(kwargs)
    #     return total_likes()

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content']
    success_url = '/'

    def form_valid(self, form): #overriding createView to add author before form submitted
        form.instance.username = self.request.user    #set author to current signed in user
        return super().form_valid(form)

    #something here for ajax


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

def friends(request):
    return render(request, 'feed/friends.html')

def messages(request):
    return render(request, 'feed/messages.html', {'username': 'ncumbo'})



def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    print("hereee")
    print(post)
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
