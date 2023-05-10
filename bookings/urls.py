from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('choose_date', views.DatePicker, name='choose_date'),
    path('reservation', views.ShoppingView.as_view(), name='reservation'),
    path('booking', views.CartView, name="booking"),
    path('posted', views.update_database, name='posted'),
]
