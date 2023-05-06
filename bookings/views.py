from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Reservation, Room, GameTime
from datetime import datetime, date
from .forms import DateForm


def dateChoiceView(request):
    form = DateForm()
    template = "date_choice.html"
    return render(request, template, {'form': form})


def resultView(request):
    template = "reservation.html"
    specific_date = request.POST['selection']
    specific_times = GameTime.objects.all()
    room_list = Room.objects.all()

    results = dayView(room_list, specific_date, specific_times)

    context = {
        'results': results,
        'selections': specific_date
    }
    return render(request, template, context)


def checkRes(room, date, time):

    if (Reservation.objects.filter(date=date, room_choice=room, time_slot=time).exists()):
        result = 45
        return result
    else:
        result = 501
        return result


def timeChecks(room, date, times):
    result = []
    for time in times:
        checked = checkRes(room, date, time)
        result.append(checked)
    return result  


def dayView(rooms, date, times):
    result = []
    for room in rooms:
        time_list = timeChecks(room, date, times)
        list_pairs = {room: time_list}
        result.append(list_pairs)
    return result    


def choiceView(request):
    template = "selected_reservation.html"
    room_data = request.POST['key']
    time_data = request.POST['value']

    specific_date = request.POST['selected_date']
    specific_times = GameTime.objects.all()
    room_list = Room.objects.all()

    results = dayView(room_list, specific_date, specific_times)

    context = {
        'room': room_data,
        'time': time_data,
        'results': results,
        'date': specific_date
    }

    return render(request, template, context)      
