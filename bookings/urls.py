from . import views
from django.urls import path

urlpatterns = [
    path('', views.dateChoiceView, name='home'),
    path('reservation/', views.resultView, name="reservation"),
    path('reservation_choices/', views.choiceView, name='reservation_picked')
]
