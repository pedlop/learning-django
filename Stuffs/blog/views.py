# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from blog.models import Post

# Create your views here.
def post_list(request) :
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts' : posts})

def post(request, id) :
    post = Post.objects.filter(id = id)
    return render(request, 'post_list.html', {'posts' : post})

def post_boot(request) :
    posts = Post.objects.all()
    return render(request, 'post_boot.html', {'posts' : posts})

