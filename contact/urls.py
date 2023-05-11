from . import views
from django.views import View
from django.urls import path

urlpatterns = [
        path('contact_us', views.ContactUs, name='contact_us'),

]