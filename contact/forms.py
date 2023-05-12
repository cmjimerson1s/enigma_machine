from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'inquiry_name',
            'inquiry_email',
            'phone_number',
            'inquiry_message',
        )
        widgets = {
            'inquiry_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'inquiry_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number'}),
            'inquiry_message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'What is your Question?'}),
        }

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['inquiry_name'].widget.attrs.update({'autofocus': True})
                self.fields['inquiry_email'].widget.attrs.update({'autofocus': True})
                self.fields['phone_number'].widget.attrs.update({'autofocus': True})
                self.fields['inquiry_message'].widget.attrs.update({'autofocus': True})



        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get('inquiry_name')
            emails = cleaned_data.get('inquiry_email')
            phone = cleaned_data.get('phone_number')
            message = cleaned_data.get('inquiry_message')

            if not name:
                self.add_error('name', 'Please enter your name.')
            if not emails:
                self.add_error('emails', 'Please enter your email.')
            if not phone:
                self.add_error('phone', 'Please enter your phone number.')
            if not message:
                self.add_error('message', 'Please enter your message.')

            return cleaned_data        
