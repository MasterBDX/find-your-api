from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from main.models import ApiGuide

class GuidesSitemap(Sitemap):
    def items(self):
        return ApiGuide.objects.all()


class StaticSitemap(Sitemap):
    def items(self):
        return ['home','list','contact']
    
    def location(self,item):
        return reverse('main:'+ item)