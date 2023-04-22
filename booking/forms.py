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

