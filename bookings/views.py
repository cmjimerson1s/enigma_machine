from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Reservation
from datetime import datetime, date
# from django.views.decorators.csrf import csrf_exempt
from .forms import DateForm


# @csrf_exempt
def reservation_view(request):
    date_today = date(2023, 5, 1)
    reservations = Reservation.objects.all()
    return render(request, 'reservation.html', {'reservations': reservations, 'date_today': date_today})


# @csrf_exempt
# def dateChoiceView(request):

#     if request.method == 'POST':
#         form = DateForm(request.POST)

#         if form.is_valid():
#             day = request.POST.get['day']
            
#             request.session['day'] = day
#             # request.session['name'] = name

#             return redirect('reservationGridView')
#     else:
#         form = DateForm()

#     return render(request, "date_choice.html", {'form': form})

def dateChoiceView(request):
    form = DateForm()
    if request.method == 'POST':
        day = request.POST.get('day')
            
        request.session['day'] = day
           

        return redirect('reservation')
   

    return render(request, "date_choice.html", {'form': form})


# def dateChoiceView(request):
#     if request.method == 'POST':
#         day = request.POST.get('day')

#         request.session['day'] = day
        
#         return redirect('reservation')

#     return render(request, "date_choice.html")


# @csrf_exempt
def reservationGridView(request):
    for o in request.POST:
        print(o)
    
    day = request.session.get('day')
    print(day)

    return render(request, "reservation.html", {'day': day})


    # for o in request.POST:
    #     print(o)
        
    # day = request.session.get('days')
    # print(day)
    
    # times = [
    #     "12:00", "14:00", "16:00", "18:00"
    # ]

    # status = checkTimeSlot(times, day)
    # return render(request, 'reservation.html', {
    #     'times': status,
    #     'day': day,
    # })


# @csrf_exempt
def checkTimeSlot(times, day):
    #Collect the timeslots that have not been booked
    x = []
    for k in times:
        #date is the model object and day should be the name to the variable stored from user input 
        if Reservation.objects.filter(date=day, time_slot=k).count() < 1:
            x.append(k)
    return x