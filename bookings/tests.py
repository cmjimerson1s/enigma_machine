import datetime
from django.test import TestCase
from .models import Room, Reservation
from .views import checkRes, timeChecks, dayView


class DayViewCheck(TestCase):

    def test_day_view(self):
        # create mock room objects
        room1 = Room.objects.create(room_name='Room 1', room_description='Description 1')
        room2 = Room.objects.create(room_name='Room 2', room_description='Description 2')
        rooms1 = str(room1)
        rooms2 = str(room2)


        # create mock reservation objects
        res1 = Reservation.objects.create(customer_name='Customer 1', customer_email='customer1@example.com', customer_phone='111111111', player_numbers=4, price=300, room_choice=room1, time_slot='14:00', date='2023-01-01')
        # define test inputs

        rooms = [rooms1, rooms2]
        date = '2023-01-01'
        times = ['14:00', '15:00', '16:00', '17:00']

        # call the function being tested
        result = dayView(rooms, date, times)

        # check that the output is correct
        expected_result = [{"Room: Room 1": [45, '15:00', '16:00', '17:00']}]

        self.assertEqual(result, expected_result)