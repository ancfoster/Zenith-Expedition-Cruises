import os
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login
from django.db.models import F
from PIL import Image
from django_countries import countries
from django.views import generic, View
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .forms import NewDestinationForm, NewTagForm, NewCruiseForm

from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests


# mapkey is the key used for mapbox maps
mapkey = os.environ.get('MAPBOX')


@staff_member_required
def NewCruise(request):
    '''
    This function creates a new cruise, fares, tickets and movements
    '''
    #Get a list of all destinations which will be passed to template
    destinations = get_destinations()
    if request.method == 'POST':
        new_cruise_form = NewCruiseForm(request.POST, request.FILES)
        if new_cruise_form.is_valid():
            # Create cruise
            name = new_cruise_form.cleaned_data['name']
            ship_id = new_cruise_form.cleaned_data['ship']
            ship = get_object_or_404(Ships, id=ship_id)
            duration = new_cruise_form.cleaned_data['duration']
            start_date = new_cruise_form.cleaned_data['start_date']
            end_date = new_cruise_form.cleaned_data['end_date']
            description = new_cruise_form.cleaned_data['description']
            tag_ids = new_cruise_form.cleaned_data.getlist('tags')
            tags = Tag.objects.filter(id__in=tag_ids)
            slug_text = f"{slugify(name)}-{start_date}"
            slug = slug_text
                #Upload results image and process
            results_image_file = new_cruise_form.cleaned_data['results_image']
            compressed_results_image = compress_uploaded_images(results_image_file, f"{slug_text}_r", 400)
            compressed_results_image.upload_to = f"cruises/{slug_text}"
                #Upload listing image and process
            listing_image_file = new_cruise_form.cleaned_data['listing_image']
            compressed_listing_image = compress_uploaded_images(results_image_file, f"{slug_text}_l", 1400)
            compressed_listing_image.upload_to = f"cruises/{slug_text}"
                #Upload map image and process 
            map_image_file = new_cruise_form.cleaned_data['map_image']
            compressed_map_image = compress_uploaded_images(results_image_file, f"{slug_text}_map", 800)
            compressed_map_image.upload_to = f"cruises/{slug_text}"
            # Save cruise
            new_cruise = Cruises.objects.create(name, ship, duration, start_date, end_date, description, slug, results_image=compressed_results_image, listing_image=compressed_listing_image, map_image=compressed_map_image)
            new_cruise.set(tags)

            my_model.tags.set(tags)

            # Create fares

            # Create tickets

            # Create ship movements

            # Return to cruises list in cruise manager
    else:
        new_cruise_form = NewCruiseForm()
    
    context = {
        'new_cruise_form': NewCruiseForm,
        'destinations': destinations,
    }
    return render(request, 'cruise_manager/new_cruise.html', context)


def get_destinations():
    '''
    This function gets a list of all the destinations
    in the destination model and returns JSON which is
    then returned as a variable in NewCruise and 
    sent to the new cruise template
    '''
    destinations = list(Destination.objects.all().order_by('name').values('id', 'name', 'country'))
    '''
    Country returns country as two-letter code,
    this needs converting to full country name.
    '''
    for destination in destinations:
        destination['country'] = get_country_name(destination['country'])
    #convert to json
    destinations_json = json.dumps(destinations)
    return destinations_json


def get_country_name(code):
    '''
    Uses django-countries library to get full country name
    from two letter country code
    '''
    return dict(countries)[code]


@staff_member_required
def NewDestination(request):
    '''
    Allows staff to create new destinations for cruises
    '''
    if request.method == 'POST':
        new_destination_form = NewDestinationForm(request.POST, request.FILES)
        if new_destination_form.is_valid():
            image = new_destination_form.cleaned_data['image']
            image_name = new_destination_form.cleaned_data['name'].replace(" ", "")
            # 960 is the maximum dimension in px
            compressed_image = compress_uploaded_images(image, image_name, 960)
            new_destination_form.instance.image = compressed_image
            new_destination_form.instance.image.field.upload_to = 'destination_img/'
            form = new_destination_form.save()
            form.save()
            return redirect('destinations')
    else:
        new_destination_form = NewDestinationForm()

    context = {
        'mapkey': mapkey,
        'new_destination_form': new_destination_form
    }
    return render(request, 'cruise_manager/new_destination.html', context)


@staff_member_required
def Destinations(request):
    '''
    This view displays all destinations in the database
    '''
    destination_queryset = Destination.objects.all().order_by('name')
    number_destinations = destination_queryset.count()
    context = {
        'number_destinations' : number_destinations,
        'destinations': destination_queryset,
    }
    return render(request, 'cruise_manager/destinations.html', context)


@staff_member_required
def NewTag(request):
    '''
    Displays the new tag form & template
    '''
    if request.method == 'POST':
        new_tag_form = NewTagForm(request.POST)
        if new_tag_form.is_valid():
            new_tag_form.save()
            return redirect('tags')
    else:
        new_tag_form = NewTagForm()
    
    context = {
        'new_tag_form': new_tag_form,
    }
    return render(request, 'cruise_manager/new_tag.html', context)


@staff_member_required
def Tags(request):
    '''
    Shows a list of created tags in cruise manager
    '''
    tag_queryset = Tag.objects.all().order_by('name')
    number_tags = tag_queryset.count()
    context = {
        'tags' : tag_queryset,
        'number_tags' : number_tags,
    }
    return render(request, 'cruise_manager/tags.html', context)


@staff_member_required
def DestinationDetail(request, slug):
    '''
    In the cruise manager app this shows the details of a 
    specific destination
    '''
    destination = get_object_or_404(Destination, slug=slug)
    context = {
        'destination' : destination,
        'mapkey': mapkey,
    }
    return render(request, 'cruise_manager/destination.html', context)


def compress_uploaded_images(image, image_name, max_dimension):
    '''
    This function compresses uploaded imagaes for end user performance,
    SEO purposes. It also removes alpha channel from PNGs for JPEG conversion.
    Uses PILLOW library.
    '''
    image = Image.open(image)
    # Code snippet by Prahlad Yeri
    if image.mode in ("RGBA", "P"):
        image = image.convert('RGB')
    # .thumbnail method resizes the uploaded images, values are max height & width  # noqa
    image.thumbnail((max_dimension, max_dimension))
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=71)
    # listing name consist of listing create form, make + model + pk fields
    image_file = InMemoryUploadedFile(image_io, None, f"{image_name}.jpeg", 'image/jpeg', image_io.tell(), None)  # noqa
    return image_file