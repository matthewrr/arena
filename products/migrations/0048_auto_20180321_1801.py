# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-21 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0047_auto_20180320_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='food',
            name='vegetarian',
        ),
        migrations.RemoveField(
            model_name='product',
            name='food_cost',
        ),
        migrations.RemoveField(
            model_name='product',
            name='profit',
        ),
    ]
