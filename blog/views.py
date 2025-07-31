from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post

# Create your views here.

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/detail.html',
        {
            'post': post,
        }
    )
