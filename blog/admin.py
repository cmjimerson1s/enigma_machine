from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'posted_date',)
    search_fields = ('blog_title','blog_content','posted_date', 'meta_tags',)
    list_filter = ('posted_date',)
    prepopulated_fields = {'slug': ('blog_title',)}