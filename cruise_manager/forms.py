from django import forms
from cruises.models import Destination, Tag, Cruises
from datetime import date, timedelta


class DateInput(forms.DateInput):
    input_type = 'date'


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


class NewCruiseModelForm(forms.ModelForm):
    class Meta:
        model = Cruises
        two_days_time = date.today() + timedelta(days=2)
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
            'results_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'map_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'listing_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'start_date': DateInput(attrs={'min': f"{two_days_time}"}),
        }
        fields = ('name', 'ship', 'duration', 'start_date', 'description',
        'results_image', 'listing_image', 'map_image', 'bookable', 'tags',)


class NewCruiseOtherFields(forms.Form):

    #Fares for each category
    verandah_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control'}))

    deluxe_verandah_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control'}))

    spa_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control'}))

    owner_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control'}))


class NewCruiseForm(forms.Form):
    '''
    This form combines the model form fields and
    the non-model form fiels into a single form.
    This form is the one that is used in the view.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.update(NewCruiseModelForm().fields)
        self.fields.update(NewCruiseOtherFields().fields)