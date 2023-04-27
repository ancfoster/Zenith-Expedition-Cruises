from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('', views.Experience, name='experience'),
    path('', views.Contact, name='contact'),
]