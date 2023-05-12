from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('inquiry_name','inquiry_email', 'phone_number','created_date',)
    search_fields = ('inquiry_name','inquiry_email', 'phone_number','inquiry_message', 'created_date',)
    list_filter = ('created_date',)
