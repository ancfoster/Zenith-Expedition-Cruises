from django import forms
from cruises.models import Destination, Tag, Cruises, Suites, SuiteCategories, Bookings
from datetime import date, timedelta


class CruisePassengerNumber(forms.Form):
    '''
    Used at start of a new booking,
    passes on the passenger number 
    and cruise
    '''
    #Fares for each category
    passengers_for_booking = forms.IntegerField(
    default=2,
    min_value=1,
    max_value=3,
    widget=forms.NumberInput(attrs={widget=forms.HiddenInput()}))