from django.contrib import admin
from .models import Reservation, Room, GameTime


admin.site.register(Room)
admin.site.register(GameTime)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date', 'room_choice', 'time_slot')
    search_fields = ('customer_name',)
    list_filter = ('room_choice', 'date')

