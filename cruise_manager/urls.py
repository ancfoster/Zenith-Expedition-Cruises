from . import views
from django.urls import path

urlpatterns = [
    path('manager/new-destination', views.NewDestination, name="new_destination"),
    path('manager/destinations', views.Destinations, name="destinations"),
    path('manager/destination/<slug>/', views.DestinationDetail, name='destination'),
    path('manager/new-tag', views.NewTag, name="new_tag"),
    path('manager/tags', views.Tags, name='tags'),
    path('manager/new-cruise', views.NewCruise, name='new_cruise'),
    path('manager/cruises', views.DisplayCruises, name='display_cruises_manager'),
]