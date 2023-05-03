from django.shortcuts import render
from django.views import generic, View
from .models import Reservation


def reservation_view(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html', {'reservations': reservations})
