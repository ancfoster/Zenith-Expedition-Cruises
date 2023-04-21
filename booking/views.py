from django.shortcuts import render, get_object_or_404, redirect
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests
from django.db.models import Count, Case, When, BooleanField
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views import generic, View

from .forms import PassengerNumberForm

# Create your views here.
def PassengerNumber(request, slug):
    '''
    Gets the cruise from the slug,
    allows user to select number of passengers
    '''
    cruise = get_object_or_404(Cruises, slug=slug)
    if request.method == 'POST':
        passenger_number_form = PassengerNumberForm(request.POST)
        if passenger_number_form.is_valid():
            print('valid')

    else:
        passenger_number_form = PassengerNumberForm()

    context = {
        'cruise' : cruise,
        'passenger_number_form': passenger_number_form
    }

    return render(request, 'booking/number_guests.html', context)