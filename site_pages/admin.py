from django.contrib import admin
from .models import Enquiry

# Register your models here.
#Enquiry model
@admin.register(Enquiry)
class EquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sent', 'responded_to')
    fields = ('name', 'sent', 'phone', 'email', 'message')
