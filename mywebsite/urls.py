from django.urls import path
from .views import(PostListView, PostDetailView)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('youtube', views.youtube, name='youtube'),
    path('bulletin', PostListView.as_view(), name='bulletin'),
    path('bulletin/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('test', views.test, name='test'),

]