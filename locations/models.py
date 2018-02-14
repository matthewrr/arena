from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    stand_location = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.stand_location
    
    def __str__(self):
        return self.stand_location