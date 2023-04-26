from django.contrib import admin

from .models import Destination, Ships, SuiteCategories, Suites, Tag, Cruises, Fares, Movements, Tickets, Bookings

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
    list_display = ('id', 'name', 'ship_image')
    fields = ('name', 'total_suites', 'info_page', 'ship_image')
    readonly_fields = fields


#Suite category model
@admin.register(SuiteCategories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    fields = ('name', 'description', 'sleeps', 'size', 'suite_image', 'suite_layout_image', 'suite_feature_list', 'category_deckplan')


#Suites model 
@admin.register(Suites)
class SuitesAdmin(admin.ModelAdmin):
    list_display = ('suite_num_name', 'ship', 'category')
    fields = ('suite_num_name', 'ship', 'category')
    readonly_fields = fields

    def has_delete_permission(self, request, obj=None):
            return False


#Tag model
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


# Cruises model
@admin.register(Cruises)
class CruisesAdmin(admin.ModelAdmin):
    list_display = ('name', 'ship', 'start_date', 'end_date', 'bookable', 'slug', 'port_number',)
    fields = ('name', 'ship', 'created_on', 'duration', 'start_date', 'end_date', 'bookable', 'slug', 'description', 'results_image', 'listing_image', 'map_image', 'tags',)
    readonly_fields = fields


#Tickets model
@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_ref', 'cruise', 'suite', 'booked', 'created_on',)
    fields = ('ticket_ref', 'ship', 'cruise', 'suite', 'booked', 'created_on',)
    readonly_fields = fields


#Movement model
@admin.register(Movements)
class Movements(admin.ModelAdmin):
    list_display = ('cruise', 'date', 'type', 'destination', 'order',)
    fields = ('cruise', 'date', 'type', 'order', 'description')
    readonly_fields = fields


#Fares model
@admin.register(Fares)
class Fares(admin.ModelAdmin):
    list_display = ('cruise', 'suite_category', 'price')
    fields = ('cruise', 'suite_category', 'price')


#Bookings model
@admin.register(Bookings)
class Bookings(admin.ModelAdmin):
    list_display = ('booking_ref', 'booked_by', 'booking_price', 'booked_on', 'ticket')
    fields = ('booking_ref', 'booked_by', 'booking_price', 'booked_on', 'ticket')
