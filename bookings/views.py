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
    choices = []
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
        result = time
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
    choice_list = request.POST['choices']
    array_choice = ReturnArray(choice_list)
    specific_times = GameTime.objects.all()
    room_list = Room.objects.all()

    results = dayView(room_list, specific_date, specific_times)
    reservation = selectionArray(selected_room, selected_time, specific_date)

    if request.method == 'POST':
        if not any(d == reservation for d in array_choice):
            array_choice.append(reservation)
            
        context = {
            'reservation': reservation,
            'choices': array_choice,
            'results': results,
            'specific_date': specific_date
        }

        return render(request, template, context)

    context = {
        'reservation': reservation,
        'choices': array_choice,
        'results': results,
        'specific_date': specific_date
    }

    return render(request, template, context)

def ReturnArray(input):
    new_input = input
    result = ast.literal_eval(new_input)

    return result      

def selectionArray(room, time, date):
    room_data = room
    time_data = time
    res_date = date
    choice_array = []
    new_dict = {date: {room_data, time_data}}

    if new_dict not in choice_array:
        choice_array.append(new_dict)

    return choice_array