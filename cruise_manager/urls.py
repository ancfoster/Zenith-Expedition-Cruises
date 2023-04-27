from . import views
from django.urls import path
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('manager/new-destination', views.NewDestination, name="new_destination"),
    path('manager/destinations', views.Destinations, name="destinations"),
    path('manager/destination/<id>/', views.DestinationDetail, name='destination'),
    path('manager/delete-destination/<id>/', views.DeleteDestination, name='delete_destination'),
    path('manager/new-tag', views.NewTag, name="new_tag"),
    path('manager/edit-destination/<id>/', views.EditDestination, name='edit_destination'),
    path('manager/tags', views.Tags, name='tags'),
    path('manager/new-cruise', views.NewCruise, name='new_cruise'),
    path('manager/cruises', views.DisplayCruises, name='display_cruises_manager'),
    path('manager/', views.Dashboard, name='dashboard'),
    path('manager/delete-tag/<id>', views.TagDelete.as_view(), name='delete_tag'),
    path('manager/edit-tag/<id>', views.EditTag, name='edit_tag'),
    path('manager/bookings', views.DisplayBookings, name='bookings'),
    path('manager/booking/<id>/', views.BookingDetails, name='booking_details'),
    path('manager/delete-booking/<id>/', views.DeleteBooking, name='delete_booking'),
    path('manager/enquiries/', views.Enquiries, name='enquiries'),
    path('manager/enquiries/<id>', views.Enquiry, name='enquiry'),


]