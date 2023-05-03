from django.db import models


class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    player_numbers = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField(auto_created=False)
    time_slot = models.CharField(max_length=5)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.time_slot} + {self.date}"
