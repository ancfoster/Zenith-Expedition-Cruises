from django.contrib import admin

from .models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests

# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    ordering = ('name',)
    fields = ('name', 'country', 'continent', 'description', 'image', 'latitude', 'longitude')