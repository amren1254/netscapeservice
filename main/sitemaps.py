# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import TutorialCategory, TutorialSeries, Tutorial


class TutorialCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return TutorialCategory.objects.all()


class TutorialSeriesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return TutorialSeries.objects.all()


class TutorialSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Tutorial.objects.all()

    def lastmod(self, obj):
        return obj.tutorial_published
