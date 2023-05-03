from . import views
from django.urls import path

urlpatterns = [
    path('reservation', views.reservation_view, name="reservation"),
    path('', views.dateChoiceView)
]
