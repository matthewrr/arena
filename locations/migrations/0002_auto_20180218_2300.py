# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-18 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='stand_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='stand_location',
            field=models.CharField(default='', max_length=200),
        ),
    ]