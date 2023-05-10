from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


def DatePicker(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        url = reverse('reservation') + f'?selected_date={selected_date}'
        return redirect(url)

    return render(request, 'date_choice.html')