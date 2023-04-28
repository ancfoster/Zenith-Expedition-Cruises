from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('experience/', views.Experience, name='experience'),
    path('contact/', views.Contact, name='contact'),
]
