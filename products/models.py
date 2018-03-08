from __future__ import unicode_literals

import random
import os

from django import forms #combine elsewhere?
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.admin import widgets
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator

from arena.utils import unique_slug_generator
from locations.models import Location

from model_utils.managers import InheritanceManager
from multiselectfield import MultiSelectField

CATEGORY = [
    ('food', 'Food'),
    ('beverage','Beverage'),
]
COURSE = [
    ('appetizer','Appetizer'),
    ('entree', 'Entree'),
    ('dessert', 'Dessert'),
]
DIET = [
    ('vegetarian', 'Vegetarian'),
    ('vegetarian_option', 'Vegetarian Option'),
    ('gluten_free','Gluten-Free'),
    ('gluten_free_option', 'Gluten-Free Option'),
]
BEVERAGE_TYPE = [
    ('alcohol', 'Alcohol'),
    ('non_alcohol', 'Non-Alcohol'),
]
ALCOHOL_TYPE = [
    ('beer', 'Beer'),
    ('wine_cider','Wine/Cider'),
    ('hard_alcohol','Hard Alcohol'),
]
SERVING_TYPE = [
    ('cup', 'Cup'),
    ('can_bottle', 'Can/Bottle'),
]

BEER_TYPE = [
    ('ale', 'Ale'),
    ('lager', 'Lager'),
    ('malt', 'Malt'),
]

WINE_CATEGORY = [
    ('white', 'White'),
    ('red', 'Red'),
    ('sparkling', 'Sparkling'),
]

WINE_TYPE = [
    ("chardonnay","Chardonnay"),
    ("sauvignon_blanc","Sauvignon Blanc"),
    ("pinot_grigio","Pinot Grigio"), #add pinot gris
    ("riesling","Riesling"),
    ("merlot","Merlot"),
    ("red_blend","Red Blend"),
    ("white_blend","White Blend"),
    ("zinfandel","Zinfandel"),
    ("pinot_noir","Pinot Noir"),
    ("syrah","Syrah"), #add siraz
    ("cabernet_sauvignon","Cabernet Sauvignon"),
    
]

BEER_STYLE = [
    ('amber', 'Amber'),
    ('pale', 'Pale'),
    ('blonde', 'Blonde'),
    ('brown', 'Brown'),
    ('ipa', 'IPA'),
    ('red', 'Red'),
    ('wheat', 'Wheat'),
    ('stout', 'Stout'),
    ('pilsner', 'Pilsner'),
    ('light', 'Light'),
]

BREWERY_TYPE = [
    ('domestic', 'Domestic'),
    ('import', 'Import'),
    ('micro', 'Micro'),
    ('craft', 'Craft'),
]

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,3759237)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    #3.6 allows final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
        )

class ProductQuerySet(models.query.QuerySet):
    
    def active(self):
        return self.filter(active=True).select_subclasses()
    
    def course(self):
        return self.filter(course='appetizer').select_subclasses()
    
    def featured(self):
        return self.filter(featured=True, active=True).select_subclasses()
    
    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query)
                   )
        return self.filter(lookups).select_subclasses()#distinct()

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def course(self):
        return self.get_queryset().course()
    
    def all(self):
        return "hello"
        #return self.get_queryset().all()

    def featured(self):
        return self.get_queryset().featured()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        
    def search(self, query):
        return self.get_queryset().active().search(query)

class Product(models.Model):

    title = models.CharField(max_length=120, default='')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=5,validators=[MinValueValidator(0)],default=0)
    location = models.ManyToManyField(Location)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    #image_exists = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True)

    filter_horizontal = ('my_m2m_field',)
    objects = InheritanceManager()

    def locations(self):
        return ",\n".join([str(item) for item in self.location.all()])

    def stand_location(self):
        return ",\n".join([item.stand_locations() for item in self.location.all()])
    
    def stand_locations(self):
        return ",\n".join([item.stand_locations() for item in self.location.all()])
    
    def stand_name(self):
        return ",\n".join([item.stand_names() for item in self.location.all()])
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
    @property
    def name(self):
        return self.title

class Food(Product):
    category = models.CharField(max_length=256, default='Food')
    course = models.CharField(max_length=256, choices=COURSE, default='')
    diet = MultiSelectField(choices=DIET, blank=True) #why pull choices name
    
    def diet_selection(self):
        return [label for value, label in self.fields['diet'].choices if value in self['diet'].value()]

class Beverage(Product):
    category = models.CharField(max_length=256, default='Beverage')
    company = models.CharField(max_length=256, default='')
    company_location = models.CharField(max_length=256, default='')
    beverage_type = models.CharField(max_length=256, choices=BEVERAGE_TYPE, default='')
    alcohol_type = models.CharField(max_length=256, choices=ALCOHOL_TYPE, default='')
    wine_category = models.CharField(max_length=256, choices=WINE_CATEGORY, blank=True)
    wine_type = models.CharField(max_length=256, choices=WINE_TYPE, blank=True)
    beer_type = models.CharField(max_length=256, choices=BEER_TYPE, blank=True)
    beer_style = models.CharField(max_length=256, choices=BEER_STYLE, blank=True)
    brewery_type = models.CharField(max_length=256, choices=BREWERY_TYPE, blank=True)
    serving_type = models.CharField(max_length=256, choices=SERVING_TYPE)
    serving_size = models.DecimalField(decimal_places=1,max_digits=3,validators=[MinValueValidator(0)],default=0)
    abv = models.DecimalField(decimal_places=1,max_digits=3,validators=[MinValueValidator(0)],default=0)
    ibu = models.DecimalField(decimal_places=0,max_digits=3,validators=[MinValueValidator(0)],default=0)
 
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Food)
pre_save.connect(product_pre_save_receiver, sender=Beverage)