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

from django import forms
from django.contrib.auth.models import User, Group
import django_filters

from locations.models import Location

from arena.utils import unique_slug_generator

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
        return self.filter(active=True)
    
    def featured(self):
        return self.filter(featured=True, active=True)
    
    def vegetarian(self):
        return self.filter(vegetarian=True, active=True)
        
    def gluten_free(self):
        return self.filter(gluten_free=True, active=True)
    
    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query)
                   )
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()
    
    def vegetarian(self):
        return self.get_queryset().vegetarian()
        
    def gluten_free(self):
        return self.get_queryset().gluten_free()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        
    def search(self, query):
        return self.get_queryset().active().search(query)
        
class Product(models.Model):
    category = models.CharField(max_length=120, default='')
    title = models.CharField(max_length=120, default='')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=5,validators=[MinValueValidator(0)],default=0)
    location = models.ManyToManyField(Location)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    alt_vegetarian = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True)
    
    filter_horizontal = ('my_m2m_field',)

    objects = ProductManager()
    
    def locations(self):
        return ",\n".join([str(item) for item in self.location.all()])
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    
    # def __unicode__(self):
    #     return self.title #python 2
    
    def __str__(self):
        return self.title
    
    @property
    def name(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)