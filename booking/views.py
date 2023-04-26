from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests
from django.db.models import Count, Case, When, BooleanField
import json
import os
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views import generic, View
from .forms import BookingForm
import stripe
from django.core.mail import send_mail


if os.path.isfile('env.py'):
    import env

STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

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
        deckplan_list.append(dict)
    
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
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_dict = request.session.get('booking_dict', None)
            if booking_dict:
                request.session['booking_dict'] = {}
            else:
                booking_dict = {}
            booking_dict['cruise'] = cruise.id
            booking_dict['number_guests'] = booking_form.cleaned_data['number_guests']
            booking_dict['selected_category'] = booking_form.cleaned_data['selected_category']
            booking_dict['selected_suite'] = booking_form.cleaned_data['selected_suite']
            booking_dict['guest_information'] = booking_form.cleaned_data['guest_information']
            request.session['booking_dict'] = booking_dict

            return redirect('payment')            

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


@login_required
def Payment(request):
    '''
    If there is a booking session display Stripe form and booking information
    '''
    booking_dict = request.session.get('booking_dict', None)
    if booking_dict:
        cruise_id = booking_dict['cruise']
        number_guests = booking_dict['number_guests']
        selected_category = booking_dict['selected_category']
        selected_suite = booking_dict['selected_suite']
        #Get cruise
        cruise = get_object_or_404(Cruises, id=cruise_id)
        #Get suite category
        suite_category = get_object_or_404(SuiteCategories, id=selected_category)
        #Getting base fare
        base_fare = get_object_or_404(Fares, cruise=cruise, suite_category=suite_category)
        base_fare_price = base_fare.price
        #Work out price to charge customer
        if number_guests == 1:
            final_fare = base_fare_price * Decimal('0.75')
        elif number_guests == 2:
            final_fare = base_fare_price
        elif number_guests == 3:
            final_fare = base_fare_price * Decimal('1.5')
        final_fare = final_fare.quantize(Decimal('0.01'))
        # Save fare in session
          #Convert to pence/cents for Stripe
        final_fare = int(final_fare * 100)
        booking_dict['final_fare'] = final_fare
        request.session['booking_dict'] = booking_dict
        #Create stripe payment intent
        intent = stripe.PaymentIntent.create(
        amount=final_fare,
        currency="gbp",
        automatic_payment_methods={"enabled": True},
        )
        client_secret = intent.client_secret

    else:
        return redirect('cruise_results')
    
    context = {
        'cruise': cruise,
        'final_fare_price': final_fare,
        'client_secret': client_secret,
        'public_key': STRIPE_PUBLIC_KEY,
    }
    return render(request, 'booking/payment.html', context)

@login_required
def PaymentConfirm(request):
    '''
    Displays the page that tells the user if the booking was successful
    and handles the session booking dictionary
    '''
    booking_dict = request.session.get('booking_dict', None)
    if booking_dict:
        cruise_id = booking_dict['cruise']
        session_id = request.session.session_key
        cruise = get_object_or_404(Cruises, id=cruise_id)
    else:
        return redirect('cruise_results')

    context = {
        'public_key' : STRIPE_PUBLIC_KEY,
        'session_id': session_id,
        'cruise': cruise,
    }
    return render(request, 'booking/status.html', context)


def ProcessBooking(request):
    '''
    Recieves a HTTP request is Stripe Payment intent
    was successful and then creates a booking.
    '''
    booking_dict = request.session.get('booking_dict')
    cruise_id = booking_dict['cruise']
    cruise = get_object_or_404(Cruises, id=cruise_id)
    number_guests = booking_dict['number_guests']
    selected_category = booking_dict['selected_category']
    selected_suite = booking_dict['selected_suite']
    suite = get_object_or_404(Suites, ship=cruise.ship, suite_num_name=selected_suite)
    booking_price = booking_dict['final_fare']
    # Get ticket object
    ticket = get_object_or_404(Tickets, cruise=cruise, suite=suite)
    ticket.booked = True
    ticket.save()
    #Generate a booking reference
    now = timezone.now()
    current_datetime = now.strftime("%d%m%Y%H%M")
    booking_ref = f"{cruise_id}{selected_suite}{current_datetime}"
    booked_by = request.user
    cruise_name_str = cruise.name

    new_booking = Bookings.objects.create(booking_ref=booking_ref,booked_by=booked_by,number_of_guests=number_guests,booking_price=booking_price,ticket=ticket,cruise_name_str=cruise_name_str)

    return HttpResponse('new booking success')

