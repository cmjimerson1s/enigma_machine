from django.test import TestCase
from .models import ContactUs

class ContactUsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ContactUs.objects.create(
            inquiry_name='John', 
            inquiry_email='john@example.com', 
            phone_number='1234567890', 
            inquiry_message='Test message',
            created_date='2023-01-01',
        )

    def test_inquiry_name_label(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        field_label = inquiry._meta.get_field('inquiry_name').verbose_name
        self.assertEqual(field_label, 'inquiry name')

    def test_created_date_label(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        field_label = inquiry._meta.get_field('created_date').verbose_name
        self.assertEqual(field_label, 'created date')

    def test_phone_number_max_length(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        max_length = inquiry._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 14)


