from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# from django.http import HttpResponse

# Create your views here.

def bulletin(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mywebsite/bulletin.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'mywebsite/bulletin.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def youtube(request):
    return render(request, 'youtube.html')

def test(request):
    return render(request, 'test.html')