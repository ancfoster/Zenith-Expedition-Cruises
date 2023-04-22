from . import views
from django.urls import path

urlpatterns = [
    path('book/<slug>/', views.NewBooking, name='new_booking'),
]