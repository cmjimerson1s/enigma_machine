from django.test import TestCase
from django.urls import reverse
from .models import ContactUs
from .forms import ContactUsForm
from django.contrib.messages import get_messages



class ContactUsTest(TestCase):

    def setUp(self):
        self.contact = ContactUs.objects.create(
            inquiry_name='Test',
            inquiry_email='test@example.com',
            phone_number='Test Inquiry',
            inquiry_message='This is a test message.',
        )
    
    def test_contact_us_view_get(self):
        """
        Test that the contact us form can be displayed via GET request
        """
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['form'], ContactUsForm)
        
    def test_contact_us_view_post_invalid_form(self):
        """
        Test that the contact us form returns an error message when an invalid form is submitted via POST request
        """
        response = self.client.post(reverse('contact_us'), {'inquiry_name': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'inquiry_email', 'Please enter your email.')
        
    def test_contact_us_view_post_valid_form(self):
        """
        Test that the contact us form successfully submits a valid form via POST request
        """
        response = self.client.post(reverse('contact_us'), {
            'inquiry_name': 'Test',
            'inquiry_email': 'test@example.com',
            'phone_number': '555-5555',
            'inquiry_message': 'Test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact_us'))
        
    def test_get_request_returns_contact_template(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_contact_us_post_view_post_invalid_form(self):
        """
        Test that the contact us post view returns an error message when an invalid form is submitted via POST request
        """
        response = self.client.post(reverse('contact_us_post'), {'inquiry_name': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertFormError(response, 'form', 'inquiry_email', 'Please enter your email.')
        
    def test_contact_us_post_view_post_valid_form(self):
        """
        Test that the contact us post view successfully submits a valid form via POST request
        """
        response = self.client.post(reverse('contact_us_post'), {
            'inquiry_name': 'Test',
            'inquiry_email': 'test@example.com',
            'phone_number': '555-555-5555',
            'inquiry_message': 'Test message'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, "Message has been sent")
    
