from django.contrib import admin

from .models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings, Guests

# Register your models here.

#Destination model
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    ordering = ('name',)
    fields = ('name', 'country', 'continent', 'description', 'image', 'latitude', 'longitude', 'slug',)


#Ships model
@admin.register(Ships)
class ShipsAdmin(admin.ModelAdmin):
    list_display = ('name', 'ship_image')
    fields = ('name', 'total_suites', 'info_page', 'ship_image')