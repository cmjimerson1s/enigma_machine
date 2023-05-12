from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError




class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    player_numbers = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_created=False)
    time_slot = models.CharField(max_length=5)
    room_choice = models.ForeignKey('Room', on_delete=models.CASCADE, related_name="room_choice", null=True)
    comment = models.TextField(max_length=300, default='')
    user_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.time_slot} + {self.date}"


class Room(models.Model):
    room_name = models.CharField(max_length=200, unique=True)
    room_description = models.TextField()
    blog_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['room_name']

    def __str__(self):
        return self.room_name


class GameTime(models.Model):
    GAME_SLOTS = [
        ('00:00','00:00'),
        ('02:00','02:00'),
        ('04:00','04:00'),
        ('06:00','06:00'),
        ('08:00','08:00'),
        ('10:00','10:00'),
        ('12:00','12:00'),
        ('14:00','14:00'),
        ('16:00','16:00'),
        ('18:00','18:00'),
        ('20:00','20:00'),
        ('22:00','22:00'),
    ]
    game_slot = models.CharField(max_length=5, choices=GAME_SLOTS)

    class Meta:
        ordering = ['game_slot']

    def clean(self):
        # Check if there is already a GameTime instance with the same game_slot value
        if GameTime.objects.filter(game_slot=self.game_slot).exists():
            raise ValidationError("A game already exists for this time slot.")

    def __str__(self):
        return self.game_slot

