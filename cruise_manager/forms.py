from django import forms
from cruises.models import Destination, Tag, Cruises
from datetime import date, timedelta


# This class creates a HTML 5 date picker element for a form field
class DateInput(forms.DateInput):
    input_type = 'date'


class NewDestinationForm(forms.ModelForm):
    '''
    Class for the form that creates a new cruise destination
    '''
    class Meta:
        model = Destination
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
        fields = "__all__"
        exclude = ('slug',)


class NewTagForm(forms.ModelForm):
    '''
    Form for creating new cruise tags
    '''
    class Meta:
        model = Tag
        fields = ('name',)


class EditTagForm(forms.ModelForm):
    '''
    Form for editing existing tags
    '''
    class Meta:
        model = Tag
        fields = ('name',)


class NewCruiseModelForm(forms.ModelForm):
    '''
    Model form class for new cruise. New cruise is form is made up
    of model form and a regular form.
    '''
    class Meta:
        model = Cruises
        two_days_time = date.today() + timedelta(days=2)
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
            'results_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'map_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'listing_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'start_date': DateInput(attrs={'min': f"{two_days_time}", 'value': f"{two_days_time}"}),
            'duration': forms.HiddenInput(attrs={'value': '2'}),
            'end_date': forms.HiddenInput(),
        }
        fields = ('name', 'ship', 'duration', 'start_date', 'description',
        'results_image', 'listing_image', 'map_image', 'bookable', 'tags',
        'end_date',)


class NewCruiseOtherFields(forms.Form):
    '''
    Regular form used in creating a new cruise. 
    This form class contains fields not in the model
    but that are used for creating a new cruise, cruise
    tickets and fares.
    '''
    #Fares for each category
    verandah_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control',
    'required': 'required'}))

    deluxe_verandah_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control',
    'required': 'required'}))

    spa_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control',
    'required': 'required'}))

    owner_suite_fare = forms.DecimalField(
    max_digits=8,
    decimal_places=2,
    widget=forms.NumberInput(attrs={'class': 'form-control',
    'required': 'required'}))

    #Movement JSON field
    movements = forms.CharField(widget=forms.HiddenInput())


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