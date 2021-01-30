from django.contrib import admin
from .models import Post, UploadImage
# Register your models here.
admin.site.register(Post)
admin.site.register(UploadImage)