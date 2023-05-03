from . import views
from django.urls import path

urlpatterns = [
    path('reservation', views.reservationGridView, name="reservation"),
    path('', views.dateChoiceView)
]
