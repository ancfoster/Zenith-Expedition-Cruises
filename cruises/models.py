from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator  # noqa

# Create your models here.

class Destination(models.Model):
    '''
    Model for different cruise destinations
    '''
    name = models.CharField(max_length=60, verbose_name="Destination Name")
    country = CountryField(blank_label="(Select Nationality)")
    ContinentChoices = [
        ('Antarctica', 'Antarctica'),
        ('Africa', 'Africa'),
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Oceania', 'Oceania')
    ]
    continent = models.CharField(choices=ContinentChoices, max_length=20)
    description = models.TextField(max_length=700, blank=False, verbose_name="Destination Description")
    image = models.ImageField(verbose_name='Destination Image')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Destination Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Destination Longitude")

    def __str__(self):
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


class SuiteCategories(models.Model):
    '''
    Each suite falls into a category. The category determines the pricing a customer pays.
    '''
    name = models.CharField(max_length=30, verbose_name="Suite Category Name")
    description = models.TextField(max_length=350, verbose_name="Suite Category Description")
    sleeps = models.PositiveSmallIntegerField(verbose_name="Category sleeps", validators=[MinValueValidator(2), MaxValueValidator(4)])
    size = models.PositiveSmallIntegerField(verbose_name="Size of suite sq m", validators=[MinValueValidator(19), MaxValueValidator(200)])
    suite_image = models.ImageField(verbose_name='Suite Image')
    suite_layout_image = models.ImageField(verbose_name='Ship Layout Image')
    suite_feature_list = models.CharField(blank=True, max_length=3000, default='', verbose_name="Suite Feature List")


    def __str__(self):
        return self.name


class Suites(models.Model):
    '''
    Each ship has a number of suites and this information is used in ticket generation.
    '''
    ship = models.ForeignKey(Ships, on_delete=models.SET_NULL, null=True, related_name="suite")
    suite_num_name = models.CharField(max_length=30, verbose_name="Suite Name/Number")
    category = models.ForeignKey(SuiteCategories, on_delete=models.SET_NULL, null=True, related_name="suite")

    def __str__(self):
        return self.suite_num_name


class Tag(models.Model):
    '''
    Tags are used to help with filtering
    '''
    name = models.CharField(max_length=25, verbose_name="Tag Name")


class Cruises(models.Model):
    '''
    Model for cruises
    '''
    name = models.CharField(max_length=120, verbose_name="Cruise Name")
    ship = models.ForeignKey(Ships, on_delete=models.SET_NULL, null=True, related_name="cruises")
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveSmallIntegerField(verbose_name="Cruise Duration", validators=[MinValueValidator(2), MaxValueValidator(199)])  # noqa
    start_date = models.DateField(verbose_name="Cruise Start Date")
    end_date = models.DateField(verbose_name="Cruise End Date")
    description = models.TextField(max_length=2000, verbose_name="Cruise Description")
    results_image = models.ImageField(verbose_name='Results Image')
    listing_image = models.ImageField(verbose_name='Listing Image')
    map_image = models.ImageField(verbose_name='Map Image')
    bookable = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name="Cruise", blank=True)

    def __str__(self):
        return self.name


class Fares(models.Model):
    '''
    This model is used to control th fares of cruises and apply offers
    '''
    cruise = models.ForeignKey(Cruises, on_delete=models.SET_NULL, null=True, related_name="fares")
    suite_category = models.ForeignKey(SuiteCategories, on_delete=models.PROTECT, related_name="fares")      
    price = models.DecimalField(max_digits=9, decimal_places=2)
    special_offer = models.BooleanField(default=False)
    offer_price = models.DecimalField(max_digits=9, decimal_places=2)


    def __str__(self):
        return self.cruise


class Movements(models.Model):
    '''
    A movement represents what ship is doing each day.
    A cruise is made up of a number of movements which are ordered.
    '''
    PossibleMovements = [
    ('D', 'Destination'),
    ('SD', 'Sea Day'),
    ('SC', 'Scenic Cruising')]
    date = models.DateField(editable=False)
    type = models.CharField(choices=PossibleMovements, max_length=2)
    ship = models.ForeignKey(Ships, on_delete=models.SET_NULL, null=True, editable=False, related_name="movement")
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True, related_name="movement")
    cruise = models.ForeignKey(Cruises, on_delete=models.CASCADE, related_name="movement")
    order = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    description = models.CharField(max_length=120, null=True, blank=True, default=None, verbose_name="Movement Description")

    def __str__(self):
        return self.date


class Tickets(models.Model):
    '''
    Tickets are automatically generated every time a cruise is created.
    A ticket is generated for every single suite onboard a ship.
    '''
    ticket_ref = models.CharField(max_length=30, editable=False, verbose_name="Ticket reference")
    ship = models.ForeignKey(Ships, null=True, on_delete=models.SET_NULL, related_name="ticket")
    cruise = models.ForeignKey(Cruises, on_delete=models.PROTECT, related_name="ticket")
    booked = models.BooleanField(default=False, verbose_name="Has ticket been booked?")
    suite = models.ForeignKey(Suites, on_delete=models.PROTECT, related_name="ticket")
    created_on = created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.ticket_ref


class Bookings(models.Model):
    '''
    Booking model, a booking is connected to a ticket.
    Bokkings can be be deleted/cancelled but not tickets, unless
    the whole cruise is deleted.
    Booking ref is generated during the booking process.
    '''
    booking_ref = models.CharField(max_length=50, editable=False)
    booked_by = models.ForeignKey(User, null=True, default=True, on_delete=models.SET_NULL, related_name='ticket')
    number_of_guests = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], verbose_name="Number of guests")
    booking_price = models.DecimalField(max_digits=9, decimal_places=2)
    booked_on = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name="booking")

    def __str__(self):
        return self.booking_ref


class Guests(models.Model):
    '''
    Guest model, each booking has at least 1 guest
    '''
    title = models.CharField(max_length=9, verbose_name="Title")
    first_name = models.CharField(max_length=25, verbose_name="First Name")
    last_name = models.CharField(max_length=25, verbose_name="Last Name")
    dob = models.DateField(max_length=25, verbose_name="Date of Birth")
    nationality = CountryField(blank_label="(Select Nationality)")
    passport_number = models.CharField(max_length=20, verbose_name="Passport Number")
    passport_expiry = models.DateField(verbose_name="Passport Expiry Date")
    address_line_1 = models.CharField(max_length=50, verbose_name="Address Line 1")
    address_line_2 = models.CharField(max_length=50, blank=True, verbose_name="Address Line 2")
    town_city = models.CharField(max_length=50, verbose_name="Town/City")
    state_county = models.CharField(max_length=50, blank=True, verbose_name="State/County")
    zip_postcode = models.CharField(max_length=12, verbose_name="Zip/Post Code")
    country_residence = CountryField(blank_label="(Select Country)")
    email = models.EmailField(max_length=70, verbose_name="Email Address")
    telephone = models.CharField(max_length=20, verbose_name="Telephone")
    dietary_requirements = models.CharField(max_length=200, blank=True, verbose_name="Dietary Requirements")
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE, related_name="guest")

    def __str__(self):
        return self.first_name.last_name



