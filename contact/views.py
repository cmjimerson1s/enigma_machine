from django.shortcuts import render
from .forms import ContactUsForm


# Create your views here.
def ContactUs(request):
    template = 'contact.html'
    form = ContactUsForm()
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'form': form,
    }

    return render(request, template, context)

def ContactUsPost(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            contact = ContactUs()
            contact.save() 
            messages.success(request, 'Form submitted successfully!')
            return render(request, 'contact_us.html')
