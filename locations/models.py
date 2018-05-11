from __future__ import unicode_literals

from django.db import models

from arena.utils import unique_slug_generator
import random
import os

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

class Location(models.Model):
    stand_name = models.CharField(max_length=200,default='')
    stand_location = models.CharField(max_length=200,default='')
    stand = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    outside_vendor = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True)
    #slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __unicode__(self):
        return self.stand_name
    
    def __str__(self):
        return self.stand_name
    
    def stand_locations(self):
        return self.stand_location
        
    def stand_names(self):
        return self.stand_name
    
    def menu(self):
        return self.image.url