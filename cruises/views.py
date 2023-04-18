from django.shortcuts import render, get_object_or_404, redirect
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests
from django.db.models import Count, Case, When, BooleanField
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views import generic, View

def CruiseDetail(request, slug):
    '''
    Displays the detail page of specific cruise
    '''
    cruise = get_object_or_404(Cruises, slug=slug)
    movements = Movements.objects.filter(cruise=cruise)
    fares = Fares.objects.filter(cruise=cruise)
    suite_cats = SuiteCategories.objects.all()
    verandah_tickets_available = Tickets.objects.filter(cruise=cruise, booked=False, suite__category__id=1).count()

    context = {
        'cruise' : cruise,
        'movements': movements,
        'suite_cats': suite_cats,
        'verandah_tickets_available' : verandah_tickets_available,
        'fares': fares,
    }
    return render(request, 'cruises/detail_view.html', context)
