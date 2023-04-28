from django.shortcuts import render, get_object_or_404, redirect
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings  # noqa
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

    context = {
        'cruise': cruise,
        'movements': movements,
        'fares': fares,
    }
    return render(request, 'cruises/detail_view.html', context)


def CruiseResults(request):
    '''
    Display list of bookable cruises
    '''
    # Tags are ysed for filtering
    tags = Tag.objects.all()
    tag_name = request.GET.get('tag')

    # Get cruises filtered by bookable flag and selected tag
    cruises = Cruises.objects.filter(
        bookable=True, tags__name=tag_name) if tag_name else Cruises.objects.filter(bookable=True)  # noqa
    cruise_fares = []
    for cruise in cruises:
        # Get the fares associated with each cruise object
        # Get the lowest of the fares
        lowest_fare = Fares.objects.filter(
            cruise=cruise).order_by('price').first()
        if lowest_fare:
            # Append to list
            cruise_fares.append({
                'cruise': cruise,
                'lowest_fare': lowest_fare.price
            })

    context = {
        'cruises': cruises,
        'cruise_fares': cruise_fares,
        'tags': tags,
    }
    return render(request, 'cruises/results_view.html', context)
