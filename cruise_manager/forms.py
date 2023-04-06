from django import forms
from cruises.models import Destination, Tag, Cruises


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


class NewCruiseForm(forms.ModelForm):
    class Meta:
        model = Cruises
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
        fields = ('name', 'ship', 'duration', 'start_date', 'description', 'results_image', 'listing_image', 'map_image', 'bookable', 'tags')
