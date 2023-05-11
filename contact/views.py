from django.shortcuts import render

# Create your views here.
def ContactUs(request):
    template = 'contact.html'

    return render(request, template)