from . import views
from django.urls import path

urlpatterns = [
    path('', views.dateChoiceView),
    path('reservation/', views.reservationGridView, name="reservation")
]
