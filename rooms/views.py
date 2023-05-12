from django.shortcuts import render

def RoomsList(request):
    template = 'room_list.html'

    return render(request, template)