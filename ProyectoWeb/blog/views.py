from django.shortcuts import render
from .models import Categoria, Post

def blog(request):
    posts = Post.objects.all()
    return render(request,'blog/blog.html',{"posts":posts})
