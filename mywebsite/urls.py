from django.urls import path
from .views import(PostListView, PostDetailView, GalleryPage)
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('gallery', views.gallery, name='gallery'),
    path('gallery', GalleryPage.as_view(), name='gallery'),
    path('youtube', views.youtube, name='youtube'),
    path('bulletin', PostListView.as_view(), name='bulletin'),
    path('bulletin/post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('test', views.test, name='test'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)