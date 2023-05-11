from django.db import models
from django.core.validators import RegexValidator

class ContactUs(models.Model):
    inquiry_id = models.AutoField(primary_key=True)
    inquiry_name = models.CharField(max_length=75)
    inquiry_email = models.EmailField()
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\+\d{2}\s\d{10}$')], help_text='Enter a 10-digit phone number.')
    created_date = models.DateTimeField(auto_now_add=True)
    inquiry_message = models.TextField()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"{self.name} Iquiry Date: {self.created_date}"
