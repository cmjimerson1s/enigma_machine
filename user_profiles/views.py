from django.shortcuts import render, redirect
from bookings.models import Reservation, GameTime, Room
from django.utils import timezone
from datetime import datetime, date


def AccountOverview(request):
    template = 'account_page.html'

    if request.user.is_authenticated:
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        user_id = request.user.id

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'user_id': user_id,
    }

    return render(request, template, context)

def AccountReservations(request):
    template = 'account_page.html'
    if request.user.is_authenticated:
        user_id = request.user.id

    entries = Reservation.objects.filter(user_id=user_id)
    reservations = []
    for entry in entries:
        res_num = entry.id
        room = entry.room_choice
        time = entry.time_slot
        date = entry.date
        res = (date, time, room, res_num)
        reservations.append(res)
        # new_date = date.date()
        # reservations.append(date)
        # reservations.append(time)
        # reservations.append(room)

    current_datetime = datetime.now()

    # Extract the date component of the datetime object
    current_date = current_datetime.date()

    context = {'entries': entries, 'reservations': reservations, 'current_date': current_date}

    return render(request, template, context)


def BookingEditSelection(request):
    template = 'reservation_edit.html'
    res_id = request.POST.get('res_id')
    res = Reservation.objects.filter(id=res_id)
    reservations = []
    for entry in res:
        room = entry.room_choice
        time = entry.time_slot
        date = entry.date
        res = (date, time, room)
        reservations.append(res)


    context = {
        'reservations': reservations, 'res_id': res_id
    }

    return render(request, template, context)

def UpdateSelection(request):
    template = 'reservation_edit.html'
    res_id = request.POST.get('res_id')
    selected_date = request.POST.get('picked_date')
    time_slot = GameTime.objects.all()
    room_list = Room.objects.all()
    results = dayView(room_list, selected_date, time_slot)

    context = {
        'results': results, 'res_id': res_id, 'selected_date': selected_date
    }

    return render(request, template, context)


def UpdateReservationEntry(request):
    res_id = request.POST.get('res_id')
    room_name = request.POST.get('key')
    time = request.POST.get('value')
    date = request.POST.get('selected_date')
    room = Room.objects.get(room_name=room_name)

    reservation = Reservation.objects.get(id=res_id)
    reservation.date = date
    reservation.time_slot = time
    reservation.room_choice = room

    reservation.save(update_fields=['date', 'time_slot','room_choice'])

    return redirect('account_bookings')












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
