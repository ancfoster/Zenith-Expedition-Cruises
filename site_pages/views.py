from django.shortcuts import render, get_object_or_404, redirect
from django.conf.urls import handler404, handler500
from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings
from django.db.models import Count, Case, When, BooleanField
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views import generic, View


# Create your views here.
def HomePage(request):
    '''
    Displays the home page
    '''
    context = {

    }
    return render(request, 'site_pages/index.html', context)