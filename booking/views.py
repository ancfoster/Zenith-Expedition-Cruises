from django.shortcuts import render, get_object_or_404, redirect
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests
from django.db.models import Count, Case, When, BooleanField
import json
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views import generic, View

from .forms import BookingForm

@login_required
def NewBooking(request, slug):
    '''
    Renders booking template form,
    receieves form input
    '''
    cruise = get_object_or_404(Cruises, slug=slug)
    if cruise.bookable == False:
        return redirect('cruise_results')
    
    movements = Movements.objects.filter(cruise=cruise)
    #Check availability of suites
    #Check availability of veranda category
    number_verandah = Tickets.objects.filter(cruise=cruise, booked=False, suite__category=1).count
    #Check availability of deluxe veranda category
    number_deluxe = Tickets.objects.filter(cruise=cruise, booked=False, suite__category=2).count
    #Check availability of spa suites
    number_spa = Tickets.objects.filter(cruise=cruise, booked=False, suite__category=3).count
    #Check availability of owner suites
    number_owner = Tickets.objects.filter(cruise=cruise, booked=False, suite__category=4).count
    # Get suite categories
    suite_categories = SuiteCategories.objects.all()
    # Get deckplans and make them available in template
    deckplan_list = []
    for suite_cat in suite_categories:
        dict = {}
        dict['category'] = suite_cat.id
        dict['url'] = suite_cat.category_deckplan.url
    
    deckplans = json.dumps(deckplan_list)

    # Get cruise fares
    fare_verandah = get_object_or_404(Fares, cruise=cruise, suite_category=1)
    fare_deluxe = get_object_or_404(Fares, cruise=cruise, suite_category=2)
    fare_spa = get_object_or_404(Fares, cruise=cruise, suite_category=3)
    fare_owner = get_object_or_404(Fares, cruise=cruise, suite_category=4)

    #Passport expiry date minimum
    cruise_end_date = cruise.end_date
    passport_min_expire = (cruise_end_date + timedelta(days=30)).strftime('%Y-%m-%d')

    if request.method == 'POST':
        print('post')

    else:
        booking_form = BookingForm()

    #Get all bookable tickets and conver to JSON
    ticket_list = []
    available_tickets = Tickets.objects.filter(cruise=cruise, booked=False)
    for ticket in available_tickets:
        dict = {}
        dict['suite_number'] = ticket.suite.suite_num_name
        dict['category'] = ticket.suite.category.id
        ticket_list.append(dict)

    suites = json.dumps(ticket_list)

    context = {
        'cruise': cruise,
        'movements': movements,
        'number_verandah' : number_verandah,
        'number_deluxe' : number_deluxe,
        'number_spa' : number_spa,
        'number_owner' : number_owner,
        'fare_verandah': fare_verandah,
        'fare_deluxe': fare_deluxe,
        'fare_spa': fare_spa,
        'fare_owner': fare_owner,
        'suite_categories' : suite_categories,
        'suites': suites,
        'booking_form': booking_form,
        'passport_min_expire': passport_min_expire,
        'deckplans': deckplans,
    }

    return render(request, 'booking/booking.html', context)
 