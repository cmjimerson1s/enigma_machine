from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Reservation, Room
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

    times = [
        "12:00", "14:00", "16:00", "18:00"
    ]

    status = checkTimeSlot(times, data)
    print(status)
    return render(request, template, {
        'times': status,
        'day': da,
    })

def resView(request):
    template = 'reservation.html'
    data = request.POST['selection']
    request.session['selection'] = data

    times = [
        "12:00", "14:00", "16:00", "18:00"
    ]
    
    results = []
    rooms = Room.objects.all()
    
    
    status = checkTimeSlot(times, data, rooms, results)

    context = {
        'times': status,
        'day': data,
        'rooms': rooms,
        'results': results
    }

    return render(request, template, context)


def checkTimeSlot(times, day, rooms, array):
    # Collect the timeslots that have not been booked
    x = []
    for k in times:
        # date is the model object and day should be the name to the variable stored from user input
        if not (Reservation.objects.filter(date=day, time_slot=k).exists()):
            x.append(k)
    array.append(x)
    return array


def checkAvailability(times, day, rooms):
    y = {}
    for room in rooms:
        time_list = checkTimeSlot(times, day, rooms)
        y = add_values_in_dict(y, room.id, time_list)
        
    return y


def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    print(sample_dict)
    return sample_dict