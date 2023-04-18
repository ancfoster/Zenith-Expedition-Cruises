from . import views
from django.urls import path

urlpatterns = [
    path('cruises/<slug>/', views.CruiseDetail, name='cruise_detail'),
]