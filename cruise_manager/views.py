import os
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login
from PIL import Image
from django.views import generic, View
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .forms import NewDestinationForm

from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests

@staff_member_required
def NewDestination(request):
    mapkey = os.environ.get('MAPBOX')
    if request.method == 'POST':
        new_destination_form = NewDestinationForm(request.POST, request.FILES)
        if new_destination_form.is_valid():
            image = new_destination_form.cleaned_data['image']
            image_name = new_destination_form.cleaned_data['name'].replace(" ", "")
            compressed_image = compress_uploaded_images(image, image_name)
            new_destination_form.instance.image = compressed_image
            new_destination_form.instance.image.field.upload_to = 'destination_img/'
            form = new_destination_form.save()
            form.save()
            return redirect('new_destination')
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
def DestinationDetail(request, slug):
    '''
    In the cruise manager app this shows the details of a 
    specific destination
    '''
    destination = get_object_or_404(Destination, slug=slug)
    context = {
        'destination' : destination,
    }
    return render(request, 'cruise_manager/destination.html', context)


def compress_uploaded_images(image, image_name):
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
    image.thumbnail((1024, 1024))
    image_io = BytesIO()
    image.save(image_io, format='JPEG', quality=71)
    # listing name consist of listing create form, make + model + pk fields
    image_file = InMemoryUploadedFile(image_io, None, f"{image_name}.jpeg", 'image/jpeg', image_io.tell(), None)  # noqa
    return image_file