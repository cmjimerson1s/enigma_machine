from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('account_overview', views.AccountOverview, name='account_overview'),
    path('account_update_view', views.AccountUpdateView, name='account_update_view'),
    path('account_update_post', views.AccountUpdatePosting, name='account_update_post'),
    path('account_bookings', views.AccountReservations, name='account_bookings'),
    path('booking_edit_selection', views.BookingEditSelection, name='booking_edit_selection'),
    path('update_booking', views.UpdateSelection, name='update_booking'),
    path('delete_booking', views.DeleteBooking, name='delete_booking'),
    path('post_update', views.UpdateReservationEntry, name='post_update'),
    path('delete_account', views.DeleteAccount, name='delete_account'),

]