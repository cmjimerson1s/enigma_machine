from django.shortcuts import render
from django.views import generic, View
from .models import Reservation
from datetime import datetime, date


def reservation_view(request):
    date_today = date(2023, 5, 1)
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html', {'reservations': reservations, 'date_today': date_today})


def dateChoiceView(request):
    return render(request, "date_choice.html",{})


def reservationGridView(request):
    day = ""
    times = [
        "12:00", "14:00", "16:00", "18:00"
    ]

    status = checkTimeSlot(times, day)
    return render(request, 'bookingSubmit.html', {
        'times':status,
    })

def checkTimeSlot(times, day):
    #Collect the timeslots that have not been booked
    x = []
    for k in times:
        #date is the model object and day should be the name to the variable stored from user input 
        if Reservation.objects.filter(date=day, time_slot=k).count() < 1:
            x.append(k)
    return x