from django.shortcuts import render, redirect
from django.contrib import messages
from bookings.models import Reservation, GameTime, Room
from django.utils import timezone
from datetime import datetime, date
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required
def AccountOverview(request):
    template = 'account_page.html'

    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    user_id = request.user.id
    email = request.user.email

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'user_id': user_id,
        'email': email,
        
    }

    return render(request, template, context)


def AccountReservations(request):
    template = 'account_bookings.html'
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

    current_datetime = datetime.now()
    current_date = current_datetime.date()

    # Extract the date component of the datetime object
    

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
    
    messages.success(request, 'Form submitted successfully!')
    reservation.save(update_fields=['date', 'time_slot','room_choice'])

    return redirect('account_overview')

def DeleteBooking(request):
    res_id = request.POST.get('res_id')
    res = Reservation.objects.filter(id=res_id)
    res.delete()

    return redirect('account_bookings')

def DeleteAccount(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user.delete()
        return redirect('home')


def AccountUpdateView(request):
    template = 'account_page_edit.html'

    if request.user.is_authenticated:
        user_id = request.user.id
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email

    

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'user_id': user_id
    }

    return render(request, template, context)

def AccountUpdatePosting(request):
    template = 'account_page.html'
    user_id = int(request.POST.get('user_id'))
    new_first_name = request.POST.get('new_first_name')
    new_last_name = request.POST.get('new_last_name')
    new_email = request.POST.get('new_email')
    new_username = request.POST.get('new_username')

    update = User.objects.get(id=user_id)
    update.username = new_username
    update.first_name = new_first_name
    update.last_name = new_last_name
    update.email = new_email
    update.save(update_fields=['username', 'first_name','last_name', 'email'])

    messages.success(request, 'Form submitted successfully!')
    context = {
        'username': new_username,
        'first_name': new_first_name,
        'last_name': new_last_name,
        'email': new_email,
        'user_id': user_id
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
