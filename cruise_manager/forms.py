from django import forms
from cruises.models import Destination, Tag

class NewDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

        fields = "__all__"
        exclude = ('slug',)


class NewTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)