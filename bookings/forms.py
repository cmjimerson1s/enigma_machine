from django import forms
from .widget import DatePickerInput

class DateForm(forms.Form):
    selection = forms.DateField(widget=DatePickerInput)

