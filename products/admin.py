from django.contrib import admin

from .models import Product
from django.contrib.admin import widgets

# Register your models here.
# Qs: How have access to obj? Why vars in quotes. Why location defined afterwards?

class ProductAdmin(admin.ModelAdmin):

    list_display = ['__str__','price','locations','slug','category','active','featured','gluten_free','vegetarian','alt_vegetarian']
    
    class Meta:
        model = Product
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        vertical = False
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Product, ProductAdmin)