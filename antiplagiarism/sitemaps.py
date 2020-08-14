from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['web:index']

    def location(self, item):
        return reverse(item)
