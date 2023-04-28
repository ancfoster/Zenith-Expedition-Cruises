from django import forms
from site_pages.models import Enquiry


class EnquiryForm(forms.ModelForm):
    '''
    Class for the form for sending a contact enquiry
    '''
    class Meta:
        model = Enquiry
        fields = ('name', 'email', 'phone', 'message')
