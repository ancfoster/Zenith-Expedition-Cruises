from . import views
from django.urls import path

urlpatterns = [
    path('manager/new-destination', views.NewDestination, name="new_destination"),
]