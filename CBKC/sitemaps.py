# core/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from fightCards.models import Event, Fighter
from tryouts.models import TryoutEvent 

class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Event.objects.all().order_by('date')

    def location(self, obj):
        return reverse('fightCardDetail', kwargs={'slug': obj.slug})

class FighterSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Fighter.objects.all().order_by('last_name', 'first_name', 'id')
    
    def location(self, obj):
        return reverse('fighter_detail', kwargs={'slug': obj.slug})



class TryoutEventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return TryoutEvent.objects.all().order_by('id')

    def location(self, obj):
        return reverse('tryout-event-detail', kwargs={'slug': obj.slug})


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['home']  # name of your urlpattern

    def location(self, item):
        return reverse(item)
