from django import forms
from cruises.models import Destination, Tag, Cruises, Suites, SuiteCategories, Bookings
from datetime import date, timedelta


class BookingForm(forms.Form):
    '''
    Form for a new cruise booking
    '''
    number_guests = forms.IntegerField(
    min_value=1,
    max_value=3,
    widget=forms.HiddenInput()
    )
    selected_category = forms.IntegerField(
    min_value=1,
    max_value=4,
    widget=forms.HiddenInput()
    )
    selected_suite = forms.IntegerField(
    widget=forms.HiddenInput()
    )
    guest_information = forms.CharField(
    widget=forms.HiddenInput()
    )

