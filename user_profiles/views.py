from django.shortcuts import render
from bookings.models import Reservation
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
        room = entry.room_choice
        time = entry.time_slot
        date = entry.date
        # new_date = date.date()
        reservations.append(date)
        reservations.append(time)
        reservations.append(room)

    current_datetime = datetime.now()

    # Extract the date component of the datetime object
    current_date = current_datetime.date()

    context = {'entries': entries, 'reservations': reservations, 'current_date': current_date}

    return render(request, template, context)
