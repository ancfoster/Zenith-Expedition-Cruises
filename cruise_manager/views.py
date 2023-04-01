import os
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from PIL import Image
from django.views import generic, View
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from .forms import NewDestinationForm

from cruises.models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests

@login_required
def NewDestination(request):
    mapkey = os.environ.get('MAPBOX')
    if request.method == 'POST':
        new_destination_form = NewDestinationForm(request.POST, request.FILES)
    else:
        new_destination_form = NewDestinationForm()
    context = {
        'mapkey': mapkey,
        'new_destination_form': new_destination_form
    }
    return render(request, 'cruise_manager/new_destination.html', context)

'''
This function compresses uploaded imagaes for end user performance,
SEO purposes. It also removes alpha channel from PNGs for JPEG conversion.
Uses PILLOW library.
'''
def compress_uploaded_images(image, image_name):
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