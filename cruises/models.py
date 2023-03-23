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
    description = models.TextField(max_length=700, blank=False, verbose_name="Destination Description")
    image = models.ImageField(verbose_name='Destination Image')
    latitude = DecimalField(max_digits=9, decimal_places=6, verbose_name="Destination Latitude")
    longitude = DecimalField(max_digits=9, decimal_places=6, verbose_name="Destination Longitude")

    def __str__(self);
        return self.name


class Ships(models.Model):
    '''
    Model for each ship
    '''
    name = models.CharField(max_length=20)
    total_suites = models.PositiveSmallIntegerField(verbose_name="Total number of suites on ship", validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    info_page = models.URLField(max_length=120, verbose_name="URL to information page")
    ship_image = models.ImageField(verbose_name='Ship Image')

    def __str__(self):
        return self.name


class Suites(models.Model):
    '''
    Each ship has a number of suites and this information is used in ticket generation.
    '''
    ship = models.ForeignKey(Ship, on_delete=models.SET_NULL, null=True, related_name="ship")
    suite_num_name = models.CharField(max_length=30, min_length=3, verbose_name="Suite Name/Number")
    category = models.ForeignKey(Suite_Category, on_delete=models.SET_NULL, null=True, related_name="Suite Category")


class Suite_Category(models.Model):
    '''
    Each suite falls into a category. The category determines the pricing a customer pays.
    '''
    name = models.CharField(max_length=30, verbose_name="Suite Category Name")
    description = models.TextField(max_length=350, verbose_name="Suite Category Description")
    sleeps = models.PositiveSmallIntegerField(verbose_name="Category sleeps", validators=[MinValueValidator(2), MaxValueValidator(4)])
    size = models.PositiveSmallIntegerField(verbose_name="Size of suite sq m", validators=[MinValueValidator(19), MaxValueValidator(200)])
    suite_image = models.ImageField(verbose_name='Suite Image')
    suite_layout_image = models.ImageField(verbose_name='Ship Layout Image')
    suite_feature_list = models.CharField(blank=True, max_length=3000, default='')


class Fares(models.Model):
    '''
    This model is used to control th fares of cruises and apply offers
    '''
    cruise = models.ForeignKey(Cruise, on_delete=models.SET_NULL, null=True, related_name="cruise")
    suite_category = models.ForeignKey(Cruise, on_delete=models.SET_NULL, null=True, related_name="suite_category")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    special_offer = models.BooleanField(initial=False)
    offer_price = models.DecimalField(max_digits=9, decimal_places=2)


class Cruises(models.Model):
    '''
    Model for cruises
    '''
    ship = models.ForeignKey(Ship)
