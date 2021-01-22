from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    post_list = Post.objects.all()
    context = {
        'object_list': post_list
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html', {})


def post(request, slug_text):
    post = Post.objects.filter(slug=slug_text)
    if post.exists():
        post = post.first()
    else:
        return HttpResponse("<h1>PAGE NOT FOUND</h1>")
    context = {
        'post': post
    }
    return render(request, 'post.html', context)


def contact(request):
    return render(request, 'contact.html', {})
