from decimal import Decimal
from django.conf import settings

def booking_context(request):

    cruise = None

    guests = None

    suite_category = None

    suite = None

    guest_details = None

    booking_status = None

    context = {
        cruise
        guests
        suite_category
        suite
        guest_details
        booking_status
    }

    return context