from django.contrib import admin
from .models import Reservation, Room, GameTime

admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(GameTime)

