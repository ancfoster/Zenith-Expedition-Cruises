from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator  # noqa

# Create your models here.


class Country(models.Model):
    '''
    Model for country, used for guest model & destination model
    '''
    name = models.CharField(max_length=50)
    continent = models.CharField(choices=ContinentChoices, max_length=20)
    ContinentChoices = [
        ('Antarctica', 'Antarctica'),
        ('Africa', 'Africa'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Oceania', 'Oceania')
    ]

    def __str__(self):
        return self.name

class Destination(models.Model):
    '''
    Model for different cruise destinations
    '''
    name = models.CharField(max_length=60, verbose_name="Destination Name")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name="Country")
    description = models.TextField(max_length=500, blank=False, verbose_name="Destination Description")
    image = models.ImageField(verbose_name='Destination Image')
    latitude = DecimalField(max_digits=9, decimal_places=6, verbose_name="Destination Latitude")
    longitude = DecimalField(max_digits=9, decimal_places=6, verbose_name="Destination Longitude")

    def __str__(self);
        return self.name



class ships(models.Model):
    '''
    Model for each ship
    '''
    name = models.CharField(max_length=20)
    total_suites = models.PositiveSmallIntegerField(verbose_name="Total number of suites on ship", validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    info_page = models.URLField(max_length=120, verbose_name="URL to information page")

    def __str__(self):
        return self.name