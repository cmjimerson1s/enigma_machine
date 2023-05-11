from django.shortcuts import render
from .models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def BlogListView(request):
    blog_posts = BlogPost.objects.all()
    template = 'blog_posts.html'
    context = {
        'blog_posts': blog_posts
    }
    return render(request, template, context)
