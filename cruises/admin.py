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
