from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.views import generic, View
from bookings.models import Room

class RoomListView(generic.ListView):
    model = Room
    queryset = Room.objects.all()
    template_name = 'room_list.html'