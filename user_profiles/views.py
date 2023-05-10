from django.shortcuts import render
from bookings.models import Reservation


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
    context = {'entries': entries}

    return render(request, template, context)