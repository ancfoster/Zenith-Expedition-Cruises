"""zenith URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from site_pages.views import handler404, handler500
from django.contrib.sitemaps.views import sitemap
from .sitemaps import CruiseSitemap

app_name = 'cruises'

sitemaps = {
    'blog':CruiseSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("site_pages.urls"), name="site_pages_urls"),
    path('', include("cruises.urls"), name="cruises_urls"),
    path('', include("cruise_manager.urls"), name="cruise_manager_urls"),
    path('', include("booking.urls"), name="booking_urls"),
    path('accounts/', include('allauth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]



