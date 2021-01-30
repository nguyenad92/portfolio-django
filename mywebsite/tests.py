from django.test import TestCase
from django.shortcuts import render
from django.views.generic import ListView, DetailView
import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
# Create your tests here.


# input = {1:2, 3:4, 5:6}

# # output = {**input}
# output = input

# print(hex(id(output)))
# print(hex(id(input)))

# path = settings.MEDIA_ROOT
# img_list = os.listdir(path + '/images')
# print(img_list)

img_list = os.listdir('media/images')
context = {'images' : img_list}
print(context)