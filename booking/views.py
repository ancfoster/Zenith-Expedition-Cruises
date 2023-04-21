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
            booking = request.session.get('booking', {})
            booking['cruise_id'] = cruise.id
            booking['number_passengers'] = passenger_number_form.cleaned_data['passengers_for_booking']
            request.session['booking'] = booking
            return redirect('booking_suite_category')

    else:
        passenger_number_form = PassengerNumberForm()
    context = {
        'passenger_number_form' : passenger_number_form,
    }
    return render(request, 'booking/number_guests.html', context)


def SuiteCategory(request):
    '''
    Allows the user to pick the suite category
    '''
    booking = request.session.get('booking', {})

    if 'number_passengers' not in booking:
        return redirect('cruise_results')
    else:
        number_passengers = booking.get('number_passengers')

    context = {
        'number_of_passengers' : number_passengers
    }
    return render(request, 'booking/suite_category.html', context)