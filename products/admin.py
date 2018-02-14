from django.contrib import admin

from .models import Product, Location
from django.contrib.admin import widgets

# Register your models here.
# Qs: How have access to obj? Why vars in quotes. Why location defined afterwards?

class ProductAdmin(admin.ModelAdmin):

    list_display = ['__str__','price','locations','slug','featured','active']
    
    class Meta:
        model = Product
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        vertical = False  # change to True if you prefer boxes to be stacked vertically
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['stand_location']
    search_fields = ['stand_location']

admin.site.register(Product, ProductAdmin)
admin.site.register(Location, LocationAdmin)