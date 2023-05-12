from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import BlogPost
from . import views 

class BlogPostListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.blogpost1 = BlogPost.objects.create(
            blog_title="Blog Post 1",
            slug="blog-post-1",
            blog_image="test.jpg",
            blog_blurb="Blurb for Blog Post 1",
            blog_content="Content for Blog Post 1",
            posted_date=timezone.now()
        )
        self.blogpost2 = BlogPost.objects.create(
            blog_title="Blog Post 2",
            slug="blog-post-2",
            blog_image="test.jpg",
            blog_blurb="Blurb for Blog Post 2",
            blog_content="Content for Blog Post 2",
            posted_date=timezone.now()
        )


    def test_blogpost_list_view(self):
        # Make a GET request to the blog list view URL and store the response in a variable
        response = self.client.get(reverse('blog-post-list'))
        # Assert that the status code of the response is 200, which means that the request was successful
        self.assertEqual(response.status_code, 200)
        #Assert that that template and content reponses match the values they should
        self.assertTemplateUsed(response, 'blog_posts.html')
        self.assertContains(response, 'Blog Post 1')
        self.assertContains(response, 'Blog Post 2')
        # Assert that the queryset of blog posts passed to the template is equal to a list of BlogPost objects as string representations
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['<BlogPost: Blog Post 2>', '<BlogPost: Blog Post 1>']
        )



class BlogPostDetailViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.blogpost = BlogPost.objects.create(
            blog_title="Blog Post",
            slug="blog-post",
            blog_image="test.jpg",
            blog_blurb="Blurb for Blog Post",
            blog_content="Content for Blog Post",
            posted_date=timezone.now()
        )

    def test_blogpost_detail_view(self):
        response = self.client.get(reverse('detail_view', args=[self.blogpost.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_post_detail.html')
        self.assertContains(response, self.blogpost.blog_title)
        self.assertContains(response, self.blogpost.blog_blurb)
        self.assertContains(response, self.blogpost.blog_content)

    def test_post(self):
        response = self.client.post(reverse('detail_view', args=[self.blogpost.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_post_detail.html')