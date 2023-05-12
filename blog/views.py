from django.shortcuts import render,get_object_or_404
from .models import BlogPost
from django.views import generic, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class BlogListView(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.all()
    template_name = 'blog_posts.html'


class BlogDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.all()
        blog = get_object_or_404(queryset, slug=slug)
        template = 'blog_post_detail.html'
        context = {
            'blog': blog
        }
        return render(request, template, context)
    
    def post(self, request, slug, *args, **kwargs):
        template = 'blog_post_detail.html'
        return render(request, template)
