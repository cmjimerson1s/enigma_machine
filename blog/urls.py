from . import views
from django.views import View
from django.urls import path

urlpatterns = [
        path('blog_list_view', views.BlogListView, name='blog_list_view'),

]