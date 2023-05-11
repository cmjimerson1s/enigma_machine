from . import views
from django.views import View
from django.urls import path

urlpatterns = [
        path('blog/', views.BlogListView, name='blog-post-list'),

]