from . import views
from django.urls import path

urlpatterns = [
    path('book/<slug>/', views.PassengerNumber, name='new_booking'),
    path('booking/suite-category/', views.SuiteCategory, name='booking_suite_category'),
]