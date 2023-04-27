from django.shortcuts import render, get_object_or_404, redirect
from django.conf.urls import handler404, handler500
from site_pages.models import Enquiry
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views import generic, View
from .forms import EnquiryForm

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
    Displays the contact page and sends contact form responses
    '''
    if request.method == 'POST':
        enquiry_form = EnquiryForm()
        if enquiry_form.is_valid():
             form.save()
             return redirect('contact')
    else:
        enquiry_form = EnquiryForm()
    context = {
        'enquiry_form' : enquiry_form,
    }
    return render(request, 'site_pages/contact.html', context)