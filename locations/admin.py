from django.contrib import admin

from .models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ['stand_location']
    search_fields = ['stand_location']
    
admin.site.register(Location, LocationAdmin)