from . import views
from django.urls import path

urlpatterns = [
    path('book/<slug>/', views.PassengerNumber, name='new_booking'),
]