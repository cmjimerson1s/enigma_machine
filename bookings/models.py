from django.db import models


class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    player_numbers = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_created=False)
    time_slot = models.CharField(max_length=5)
    room_choice = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="room_choice", null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.time_slot} + {self.date}"


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    room_description = models.TextField()

    class Meta:
        ordering = ['room_name']

    def __str__(self):
        return self.room_name
