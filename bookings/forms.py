from django import forms
from .widget import DatePickerInput

class DateForm(forms.Form):
    selection = forms.DateField(widget=DatePickerInput)


class MyForm(forms.Form):
    key = forms.HiddenInput()
    value = forms.HiddenInput()
    selected_date = forms.HiddenInput()
