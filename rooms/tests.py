from django.test import TestCase
from django.urls import reverse
from bookings.models import Room
from django.utils import timezone

class TestRoomListView(TestCase):

    def setUp(self):
        self.room1 = Room.objects.create(room_name='Room 1', room_description='Description 1')
        self.room2 = Room.objects.create(room_name='Room 2', room_description='Description 2')
        self.url = reverse('rooms')

    def test_room_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'room_list.html')
        self.assertQuerysetEqual(response.context['object_list'], [repr(self.room1), repr(self.room2)], ordered=False)
