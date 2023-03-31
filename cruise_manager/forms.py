from django import forms
from cruises.models import Destination

class NewDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

        fields = "__all__"
        exclude = ('slug',)