from django import forms
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput


class DateForm(forms.Form):
    day = forms.DateField(widget=DatePickerInput)
