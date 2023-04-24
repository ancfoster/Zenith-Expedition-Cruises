from . import views
from django.urls import path

urlpatterns = [
    path('book/<slug>/', views.NewBooking, name='new_booking'),
    path('payment', views.Payment, name='payment'),
    path('payment/success', views.Success, name='success'),
    path('payment/process', views.stripe_webhook, name='payment_success'),
]