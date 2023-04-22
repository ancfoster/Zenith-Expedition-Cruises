from django import forms
from cruises.models import Destination, Tag, Cruises, Suites, SuiteCategories, Bookings
from datetime import date, timedelta


class PassengerNumberForm(forms.Form):
    '''
    Used at start of a new booking,
    passes on the passenger number 
    and cruise
    '''
    passengers_for_booking = forms.IntegerField(
    min_value=1,
    max_value=3,
    widget=forms.HiddenInput()
    )


class SuiteCategoryForm(forms.Form):
    '''
    Allows user to select suite category
    during booking process
    '''
    suite_category = forms.IntegerField(
        max_length=1,
        widget=forms.HiddenInput()
    )
