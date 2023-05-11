from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('account_overview', views.AccountOverview, name='account_overview'),
    path('account_bookings', views.AccountReservations, name='account_bookings'),
    path('booking_edit_selection', views.BookingEditSelection, name='booking_edit_selection'),
    path('update_booking', views.UpdateSelection, name='update_booking'),
    path('post_update', views.UpdateReservationEntry, name='post_update'),

]