from django.contrib import admin

from .models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ['stand_name','stand_location', 'active', 'featured', 'outside_vendor']
    search_fields = ['stand_name','stand_location']
    
admin.site.register(Location, LocationAdmin)