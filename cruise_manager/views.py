import os
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.forms import modelformset_factory
from django.utils.text import slugify
from django.db.models import F
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
import uuid
from PIL import Image
from django_countries import countries
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .forms import NewDestinationForm, NewTagForm, NewCruiseForm, EditTagForm, EditDestinationForm, EditCruiseForm, EditFareForm

from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings
from site_pages.models import Enquiry

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
            ship = new_cruise_form.cleaned_data['ship']
            duration = new_cruise_form.cleaned_data['duration']
            start_date = new_cruise_form.cleaned_data['start_date']
            end_date = new_cruise_form.cleaned_data['end_date']
            description = new_cruise_form.cleaned_data['description']
            port_number = 0
            # tags = new_cruise_form.cleaned_data['tags']
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
            new_cruise = Cruises.objects.create(
            name=name,
            ship=ship,
            duration=duration,
            start_date=start_date,
            end_date=end_date,
            description=description,
            slug=slug,
            port_number = port_number,
            results_image=compressed_results_image,
            listing_image=compressed_listing_image,
            map_image=compressed_map_image,
            )
                #Adds tags
            tags = new_cruise_form.cleaned_data['tags']
            for tag in tags:
                new_cruise.tags.add(tag)

                #Get ID of newly created cruise for use in creating fares, tickets           
            cruise_id = new_cruise.id
            # Create fares
                #Verandah suite fare
            verandah_suite_fare = new_cruise_form.cleaned_data['verandah_suite_fare']
            new_verandah_suite_fare = Fares.objects.create(
                suite_category=SuiteCategories.objects.get(id=1),
                cruise=Cruises.objects.get(id=cruise_id),
                price=verandah_suite_fare,
            )
                #Deluxe verandah fare
            deluxe_verandah_suite_fare = new_cruise_form.cleaned_data['deluxe_verandah_suite_fare']
            new_deluxe_verandah_suite_fare = Fares.objects.create(
                suite_category=SuiteCategories.objects.get(id=2),
                cruise=Cruises.objects.get(id=cruise_id),
                price=deluxe_verandah_suite_fare,
            )
                #Spa suite fare
            spa_suite_fare = new_cruise_form.cleaned_data['spa_suite_fare']
            new_spa_suite_fare = Fares.objects.create(
                suite_category=SuiteCategories.objects.get(id=3),
                cruise=Cruises.objects.get(id=cruise_id),
                price=spa_suite_fare,
            )
                #owner suite fare
            owner_suite_fare = new_cruise_form.cleaned_data['owner_suite_fare']
            new_owner_suite_fare = Fares.objects.create(
                suite_category=SuiteCategories.objects.get(id=4),
                cruise=Cruises.objects.get(id=cruise_id),
                price=owner_suite_fare,
            )
            # Create tickets
                #Get the number of suites for the required ship
            suite_tickets = Suites.objects.filter(ship=ship)

            for suite_ticket in suite_tickets:
                new_ticket = Tickets.objects.create(
                    ship = ship,
                    cruise = Cruises.objects.get(id=cruise_id),
                    suite = suite_ticket,
                    ticket_ref = str(uuid.uuid4())[:8],
                )

            # Create ship movements
                # Convert JSON movements to Python dictionary
            movements_json = new_cruise_form.cleaned_data['movements']
            movements_dict = json.loads(movements_json)
                # For each dictionary item create a movement
            for movement in movements_dict:
                order = movement['day']
                date = movement['backEndDate']
                type = movement['type']
                if type != 'D':
                    destination = None
                    description = movement['description']
                else:
                    destination = Destination.objects.get(id=movement['destination'])
                    description = None
                #Create each movement object
                new_movement = Movements.objects.create(
                    cruise = Cruises.objects.get(id=cruise_id),
                    order = order,
                    date = date,
                    type = type,
                    destination = destination,
                    description = description,
                    ship = ship,
                )
            cruise = Cruises.objects.get(id=cruise_id)
            '''
            Now that the movements have been created, the number of
            unique destinations can be calculated. This number can then
            be applued to the cruise that was created in this function.
            '''
            destination_count = Movements.objects.filter(cruise=cruise, type='D').values('destination').distinct().count()
            cruise.port_number = destination_count
            cruise.save()
            # Return to cruises list in cruise manager
            return redirect('display_cruises_manager')
        else:
            new_cruise_form = NewCruiseForm()
    else:
        new_cruise_form = NewCruiseForm()
    
    context = {
        'new_cruise_form': NewCruiseForm,
        'destinations': destinations,
    }
    return render(request, 'cruise_manager/new_cruise.html', context)


@staff_member_required
def DisplayCruises(request):
    '''
    Dipslays cruises in the cruise manager
    '''
    cruises_queryset = Cruises.objects.all().order_by('name')
    number_cruises = cruises_queryset.count()
    context = {
        'number_cruises' : number_cruises,
        'cruises': cruises_queryset,
    }
    return render(request, 'cruise_manager/cruises.html', context)


@staff_member_required
def EditCruise(request, id):
    '''
    Allows editing of cruise fields and 
    associated cruise fares
    '''
    cruise = get_object_or_404(Cruises, id=id)

    FaresFormSet = modelformset_factory(Fares, form=EditFareForm, extra=0)
    if request.method == 'POST':
        cruise_form = EditCruiseForm(request.POST, instance=cruise)
        fares_formset = FaresFormSet(request.POST, queryset=Fares.objects.filter(cruise=cruise))
        if cruise_form.is_valid() and fares_formset.is_valid():
            # Save the updates to the cruise object and its associated fares
            cruise_form.save()
            fares_formset.save()
            return redirect('display_cruise', id=id)
    else:
        # Initialize the Cruise form and Fares formset with the data from the cruise object and its associated fares
        cruise_form = EditCruiseForm(instance=cruise)
        fares_formset = FaresFormSet(queryset=Fares.objects.filter(cruise=cruise))

    context = {
        'cruise': cruise,
        'cruise_form': cruise_form,
        'fares_formset': fares_formset,
    }
    return render(request, 'cruise_manager/edit_cruise.html', context)


@staff_member_required
def DeleteCruise(request, id):
    '''
    Deletes a cruise and associated tickets
    Tickets must be deleted first as they are
    protected
    '''
    #Get cruise object and ticket objects
    cruise = get_object_or_404(Cruises, id=id)
    tickets = Tickets.objects.filter(cruise=cruise)
    # Delete tickets and cruises
    if request.method == 'POST':
        tickets.delete()
        cruise.delete()
        return redirect('display_cruises_manager')
    context = {
        'cruise': cruise,
    }
    return render(request, 'cruise_manager/delete_cruise.html', context)


@staff_member_required
def CruiseDetail(request, id):
    '''
    Displays the detail of a cruise
    '''
    cruise = get_object_or_404(Cruises, id=id)
    fares = Fares.objects.filter(cruise=cruise)
    movements = Movements.objects.filter(cruise=cruise)
    context = {
        'cruise':cruise,
        'fares':fares,
        'movements':movements,
    }
    return render(request, 'cruise_manager/cruise.html', context)


@staff_member_required
def DisplayBookings(request):
    '''
    Displays a list of booings in cruise manager
    '''
    bookings_queryset = Bookings.objects.all()
    number_bookings = bookings_queryset.count()
    context = {
        'number_bookings' : number_bookings,
        'bookings': bookings_queryset,
    }
    return render(request, 'cruise_manager/bookings.html', context)


@staff_member_required
def BookingDetails(request, id):
    '''
    Displays the details of an individual booking
    '''
    booking = get_object_or_404(Bookings, id=id)
    price = booking.booking_price / 100
    context = {
        'booking' : booking,
        'price': price,
    }
    return render(request, 'cruise_manager/booking.html', context)


@staff_member_required
def DeleteBooking(request, id):
    '''
    Deletes a book and makes the assosciated ticket available again
    '''
    booking = get_object_or_404(Bookings, id=id)
    
    if request.method == 'POST':
        ticket = booking.ticket
        booking.delete()
        ticket.booked = False
        ticket.save()
        return redirect('bookings')
    context = {
        'booking' : booking,
    }
    return render(request, 'cruise_manager/delete_booking.html', context)


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
def EditDestination(request, id):
    '''
    Displays the edit tag form & template, and updates the tag if the form is submitted
    '''
    destination = get_object_or_404(Destination, id=id)

    if request.method == 'POST':
        edit_destination_form = EditDestinationForm(request.POST, instance=destination)
        if edit_destination_form.is_valid():
            edit_destination_form.save()
            return redirect('destinations')
    else:
        edit_destination_form = EditDestinationForm(instance=destination)
    
    context = {
        'edit_destination_form': edit_destination_form,
        'destination': destination,
        'mapkey': mapkey
    }
    return render(request, 'cruise_manager/edit_destination.html', context)


@staff_member_required
def DeleteDestination(request, id):
    '''
    Deletes a destination provided it isn't being used in a movement
    '''
    destination = get_object_or_404(Destination, id=id)
    related_movements = Movements.objects.filter(destination=destination).count()
    if request.method == 'POST':
        destination.delete()
        return redirect('destinations')
    context = {
        'destination' : destination,
        'related_movements' : related_movements,
    }
    return render(request, 'cruise_manager/delete_destination.html', context)


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
def EditTag(request, id):
    '''
    Displays the edit tag form & template, and updates the tag if the form is submitted
    '''
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        edit_tag_form = EditTagForm(request.POST, instance=tag)
        if edit_tag_form.is_valid():
            edit_tag_form.save()
            return redirect('tags')
    else:
        edit_tag_form = EditTagForm(instance=tag)
    
    context = {
        'edit_tag_form': edit_tag_form,
        'tag': tag,
    }
    return render(request, 'cruise_manager/edit_tag.html', context)


#As this is a class view a different method is used to enforce staff access
@method_decorator(user_passes_test(lambda u: u.is_staff), name='dispatch')
class TagDelete(DeleteView):
    '''
    Deletes a tag
    '''
    template_name = 'cruise_manager/delete_tag.html'

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Tag, id=id)

    def get_success_url(self):
        return reverse('tags')


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
def DestinationDetail(request, id):
    '''
    In the cruise manager app this shows the details of a 
    specific destination
    '''
    destination = get_object_or_404(Destination, id=id)
    context = {
        'destination' : destination,
        'mapkey': mapkey,
    }
    return render(request, 'cruise_manager/destination.html', context)


@staff_member_required
def Dashboard(request):
    '''
    Displays dashboard in cruise manager
    '''
    # Calculate revenue in the past 90 days
    date_90_days_ago = timezone.now() - timedelta(days=90)
    revenue = Bookings.objects.filter(booked_on__gte=date_90_days_ago).aggregate(total_booking_price=Sum('booking_price'))['total_booking_price']
    #Convert from pence to pounds
    revenue = revenue / 100
    # Get number of bookings in pas 90 days
    bookings = Bookings.objects.filter(booked_on__gte=date_90_days_ago).count()
    # Get number of enquiries that need responding to
    respond_to = Enquiry.objects.filter(responded_to=False).count()
    context = {
        'revenue' : revenue,
        'bookings' : bookings,
        'respond_to' : respond_to,
    }
    return render(request, 'cruise_manager/dashboard.html', context)


@staff_member_required
def Enquiries(request):
    '''
    Displays a list of receieved enquiries
    '''
    enquiries = Enquiry.objects.order_by('-sent')
    enquiries_number = enquiries.count()
    unresponded_count = Enquiry.objects.filter(responded_to=False).count()
    context = {
        'enquiries' : enquiries,
        'enquiries_number' : enquiries_number,
        'unresponded_count' : unresponded_count,
    }
    return render(request, 'cruise_manager/enquiries.html', context)


@staff_member_required
def EnquiryDetail(request, id):
    '''
    Displays a specific enqiry message with actions
    '''
    enquiry = get_object_or_404(Enquiry, id=id)
    context = {
        'enquiry' : enquiry,
    }
    return render(request, 'cruise_manager/enquiry.html', context)


@staff_member_required
def DeleteEnquiry(request, id):
    '''
    Deletes an enquiry, but presents action confirmation first
    '''
    enquiry = get_object_or_404(Enquiry, id=id)
    
    if request.method == 'POST':
        enquiry.delete()
        messages.add_message(request, messages.INFO, 'The enquiry was deleted')
        return redirect('enquiries')
    context = {
        'enquiry' : enquiry,
    }
    return render(request, 'cruise_manager/delete_enquiry.html', context)


def EnquiryStatus(request, id):
    enquiry = get_object_or_404(Enquiry, id=id)
     # toggle status
    enquiry.responded_to = not enquiry.responded_to
    enquiry.save()
    messages.add_message(request, messages.INFO, 'Enquiry status updated')
    return redirect('enquiry', id=id)


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