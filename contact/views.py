from django.shortcuts import render

# Create your views here.
def ContactUs(request):
    template = 'contact.html'
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
    }

    return render(request, template, context)