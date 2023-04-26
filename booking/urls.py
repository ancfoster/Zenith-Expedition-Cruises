from . import views
from django.urls import path

urlpatterns = [
    path('book/<slug>/', views.NewBooking, name='new_booking'),
    path('payment', views.Payment, name='payment'),
    path('payment/status', views.PaymentConfirm, name='payment_confirm'),
    path('payment/booking', views.ProcessBooking, name='process_booking'),
]