from . import views
from django.urls import path

urlpatterns = [
    path('', views.dateChoiceView, name='home'),
    path('reservation/', views.resView, name="reservation")
]
