from . import views
from django.views import View
from django.urls import path

urlpatterns = [
        path('contact_us', views.ContactUs, name='contact_us'),
        path('contact_us_post', views.ContactUs, name='contact_us_post'),

]