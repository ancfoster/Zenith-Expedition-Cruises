from django.shortcuts import render, get_object_or_404, redirect
from django.conf.urls import handler404, handler500
from cruises.models import Destination
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


def Experience(request):
    '''
    Displays the contact page page
    '''
    context = {
    }
    return render(request, 'site_pages/experience.html', context)


def Contact(request):
    '''
    Displays the contact page page
    '''
    context = {
    }
    return render(request, 'site_pages/contact.html', context)