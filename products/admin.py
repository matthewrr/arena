from django.contrib import admin
from django.contrib.admin import widgets
from django.db import models
from django.forms import CheckboxSelectMultiple

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Product, Food, Beverage
from .filters import DropdownFilter

# Register your models here.
# Qs: How have access to obj? Why vars in quotes. Why location defined afterwards?

class FoodResource(resources.ModelResource):

    class Meta:
        model = Food

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','price','locations','slug','active']
    
    class Meta:
        model = Product
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        vertical = False
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            vertical,
        )
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

class FoodAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['__str__','price','course','slug','active','image_uploaded', 'vegetarian','gluten_free']
    list_filter = (
        ('location__stand_name',DropdownFilter),
        'active','course','vegetarian','gluten_free',
    )
    search_fields = (
        'title', 'description',
    )
    exclude = ('category','stand','diet')

    resource_class = FoodResource

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