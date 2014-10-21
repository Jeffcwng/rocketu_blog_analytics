from django.contrib import admin

# Register your models here.
from analytics.models import Page, Location, View

admin.site.register(Page)
admin.site.register(Location)
admin.site.register(View)
