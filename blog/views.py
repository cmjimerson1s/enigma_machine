from django.shortcuts import render

def BlogListView(request):
    template = 'blog_posts.html'
    blog_list = Post.objects.all.order_by("-created_on")
    paginate_by = 6

    return render(request, template)