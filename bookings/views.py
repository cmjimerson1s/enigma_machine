from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Reservation
from datetime import datetime, date
from .forms import DateForm


def reservation_view(request):
    date_today = date(2023, 5, 1)
    reservations = Reservation.objects.all()
    return render(
        request,
        "reservation.html",
        {"reservations": reservations, "date_today": date_today},
    )


def dateChoiceView(request):
    form = DateForm()
    template = "date_choice.html"
    return render(request, template, {'form': form})


def reservationGridView(request):
    data = request.POST['selection']
    template = 'reservation.html'
    context = {
        'selection': data
    }
    request.session['selection'] = data
    return render(request, template, context)

    # times = [
    #     "12:00", "14:00", "16:00", "18:00"
    # ]

    # status = checkTimeSlot(times, day)
    # return render(request, 'reservation.html', {
    #     'times': status,
    #     'day': day,
    # })


def checkTimeSlot(times, day):
    # Collect the timeslots that have not been booked
    x = []
    for k in times:
        # date is the model object and day should be the name to the variable stored from user input
        if Reservation.objects.filter(date=day, time_slot=k).count() < 1:
            x.append(k)
    return x
