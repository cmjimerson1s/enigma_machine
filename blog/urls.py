from . import views
from django.views import View
from django.urls import path

urlpatterns = [
        path('blog-post-list', views.BlogListView.as_view(), name='blog-post-list'),
        path('<slug:slug>', views.BlogDetailView.as_view(), name='detail_view')

]