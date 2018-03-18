from django.contrib import admin
from django.contrib.admin import widgets
from django.db import models
from django.forms import CheckboxSelectMultiple

from .models import Product, Food, Beverage
from .filters import DropdownFilter

# Register your models here.
# Qs: How have access to obj? Why vars in quotes. Why location defined afterwards?

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','price','locations','slug','active','featured']
    
    class Meta:
        model = Product
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        vertical = False
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class FoodAdmin(admin.ModelAdmin):
    list_display = ['__str__','price','slug','active','featured', 'image_uploaded']
    list_filter = (
        ('location__stand_name',DropdownFilter),
        'active','diet','course',
    )
    search_fields = (
        'title', 'description',
    )
    exclude = ('category',)
    
    class Meta:
        model = Food

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        vertical = False
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(FoodAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    
class BeverageAdmin(admin.ModelAdmin):
    list_display = ['__str__','price','locations','slug','active','featured','image_uploaded']
    exclude = ('category',)
    
    class Meta:
        model = Beverage
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        vertical = False
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(BeverageAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Product, ProductAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Beverage, BeverageAdmin)