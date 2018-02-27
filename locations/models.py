from __future__ import unicode_literals

from django.db import models

from arena.utils import unique_slug_generator

class Location(models.Model):
    stand_name = models.CharField(max_length=200,default='')
    stand_location = models.CharField(max_length=200,default='')
    active = models.BooleanField(default=True)
    outside_vendor = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add = True)
    #slug = models.SlugField(blank=True, unique=True)
    #image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __unicode__(self):
        return self.stand_name
    
    def __str__(self):
        return self.stand_name
    
    def stand_locations(self):
        return self.stand_location