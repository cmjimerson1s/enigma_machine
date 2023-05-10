from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('', views.DatePicker, name='home'),
    path('reservation', views.ShoppingView.as_view(), name='reservation'),
]
