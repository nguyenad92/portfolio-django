from django.shortcuts import render
from .models import Post, UploadImage
from django.views.generic import ListView, DetailView
import os
from django.conf import settings
from django.templatetags.static import static
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
    path = settings.MEDIA_ROOT
    # img_list = os.listdir(path + '/images')
    img_list = os.listdir(path)
    context = {'images' : img_list}
    return render(request, 'gallery.html', context)

def youtube(request):
    return render(request, 'youtube.html')

def test(request):
    return render(request, 'test.html')

class GalleryPage(ListView):
    model = UploadImage
    print(type(UploadImage))
    template_name = 'gallery.html'
    context_object_name = 'images'