from django import forms
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput


class ExampleForm(forms.Form):
    day = forms.DateField(widget=DatePickerInput)
