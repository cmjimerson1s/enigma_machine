from django.shortcuts import render
from django.views import generic, View
from .models import Reservation
from datetime import datetime, date


def reservation_view(request):
    date_today = date(2023, 5, 1)
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html', {'reservations': reservations, 'date_today': date_today})
