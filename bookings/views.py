from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import Reservation, GameTime, Room
import ast


def DatePicker(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        url = reverse('reservation') + f'?selected_date={selected_date}'
        if 'cart' not in request.session:
            request.session['cart'] = []
        return redirect(url)

    return render(request, 'date_choice.html')

class ShoppingView(View):
    def get(self, request):
        # Get the items to display on the page
        specific_date = request.GET.get('selected_date')
        specific_times = GameTime.objects.all()
        room_list = Room.objects.all()
        results = dayView(room_list, specific_date, specific_times)

        context = {'results': results, 'specific_date': specific_date}
        return render(request, 'reservation.html', context)
    
    def post(self, request):
        key = request.POST.get('key')
        value = request.POST.get('value')
        specific_date = request.POST.get('specific_date')

        # Check if the item is already in the cart
        cart = request.session.get('cart', [])
        for item in cart:
            if item['key'] == key and item['value'] == value and item['specific_date'] == specific_date:
                # If the item already exists in the cart, do not add it again
                break
        else:
            # If the item does not exist in the cart, add it to the cart
            item = {'key': key, 'value': value, 'specific_date': specific_date}
            cart.append(item)
            request.session['cart'] = cart


        if 'delete-all' in request.POST:
            # Remove all items from the cart
            request.session.pop('cart', None)
        elif 'delete-item' in request.POST:
            # Get the key, value, and specific_date of the item to remove
            selected = request.POST.get('delete-item')
            key, value, specific_date = selected.split("|")
            # Find the item in the cart and remove it
            for item in request.session.get('cart', []):
                if item['key'] == key and item['value'] == value and item['specific_date'] == specific_date:
                    request.session['cart'].remove(item)
                    request.session.modified = True

                    break
        # Get the updated items to display on the page, including the user's cart


        specific_date = request.GET.get('selected_date')
        specific_times = GameTime.objects.all()
        room_list = Room.objects.all()
        results = dayView(room_list, specific_date, specific_times)
        cart = [item for item in request.session.get('cart', []) if item.get('key') and item.get('value') and item.get('specific_date')]
        context = {'results': results, 'cart': cart, "specific_date": specific_date}
        return render(request, 'reservation.html', context)


def CartView(request):
    cart = request.GET.get('cart')
    string = cart.replace('[', '').replace(']', '').replace('"', '')
    game_data = ast.literal_eval(string)
    if isinstance(game_data, dict):
    # if dataset is a dictionary, convert it to a tuple
        dataset = (game_data,)
    else:
        dataset = game_data
    context = {'data': dataset,}
    return render(request, 'selected_reservation.html', context, )

def update_database(request):
    cart = request.GET.get('data')
    string = cart.replace('[', '').replace(']', '').replace('"', '')
    game_data = ast.literal_eval(string)
    if isinstance(game_data, dict):
    # if dataset is a dictionary, convert it to a tuple
        dataset = (game_data,)
    else:
        dataset = game_data
    if request.method == 'POST':
        for item in dataset:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            numbers = request.POST.get('number')
            price = request.POST.get('price')
            date = item['specific_date']
            room_name = item['key']
            time = item['value']
            commnent = request.POST.get('comment')
            room = Room.objects.get(room_name=room_name)

            # Create a new instance of the Reservation model and set its attributes
            instance = Reservation()
            instance.customer_name = name
            instance.customer_email = email
            instance.customer_phone = phone
            instance.player_numbers = numbers
            instance.price = price
            instance.date = date
            instance.room_choice = room
            instance.time_slot = time
            instance.comment = comment
            instance.save()
    del request.session['cart']
    return HttpResponse('Data saved successfully.')


def checkRes(room, date, time):

    if (Reservation.objects.filter(date=date, room_choice=room, time_slot=time).exists()):
        result = 45
        return result
    else:
        result = time
        return result


def timeChecks(room, date, times):
    result = []
    for time in times:
        checked = checkRes(room, date, time)
        result.append(checked)
    return result  


def dayView(rooms, date, times):
    result = []
    for room in rooms:
        time_list = timeChecks(room, date, times)
        list_pairs = {room: time_list}
        result.append(list_pairs)
    return result    