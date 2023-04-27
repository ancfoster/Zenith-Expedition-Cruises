from django.contrib.sitemaps import Sitemap
from cruises.models import Cruises

 
class CruiseSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Cruises.objects.all()

    def lastmod(self, obj):
        return obj.created_on
        
    def location(self,obj):
        return '/%s' % (obj.slug)