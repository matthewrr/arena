from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    stand_name = models.CharField(max_length=200,default='')
    stand_location = models.CharField(max_length=200,default='')
    
    def __unicode__(self):
        return self.stand_name
    
    def __str__(self):
        return self.stand_name
    
    def stand_locations(self):
        return self.stand_location