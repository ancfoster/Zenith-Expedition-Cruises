from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests
from django.db.models import Count, Case, When, BooleanField
import json
import os
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
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
        final_fare = int(final_fare * 100)

        session_id = request.session.session_key

        intent = stripe.PaymentIntent.create(
        amount=final_fare,
        currency="gbp",
        metadata={"session_id" : session_id},
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
def Success(request):
    context = {
        'public_key' : STRIPE_PUBLIC_KEY,
    }
    return render(request, 'booking/success.html', context)

@csrf_exempt
def ProcessSuccess(request):
    if request.method == 'POST':
        try:
            # parse the request body as json
            data = json.loads(request.body)
            # do something with the data 
            print("Test success")
       
            subject = 'Subject of the Email'
            message = 'This is the message body'
            from_email = 'zenithexpeditioncruises@gmail.com'
            recipient_list = ['a.foster@outlook.com',]

            send_mail(subject, message, from_email, recipient_list)

            return HttpResponse('Success')
        except json.JSONDecodeError:
            result = {'status': 'error', 'message': 'Invalid JSON'}
    else:
        result = {'status': 'error', 'message': 'Invalid request method'}
