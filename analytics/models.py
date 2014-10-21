from django.db import models
import datetime

class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u"{}".format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ['city', 'country', 'region']

    def __unicode__(self):
        return u"{}, {} {}".format(self.city, self.region, self.country)


class View(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    page = models.ForeignKey(Page)
    location = models.ForeignKey(Location,blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return u"{} by {} @ {}".format(self.ip_address, self.location, self.timestamp)
