from django import forms
from cruises.models import Enquiry


class NewDestinationForm(forms.ModelForm):
    '''
    Class for the form for sending a contact enquiry
    '''
    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'phone', 'message')