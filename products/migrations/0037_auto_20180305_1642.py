# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-05 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_auto_20180302_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='beer_style',
            field=models.CharField(blank=True, choices=[('amber', 'Amber'), ('pale', 'Pale'), ('blonde', 'Blonde'), ('brown', 'Brown'), ('ipa', 'IPA'), ('red', 'Red'), ('wheat', 'Wheat'), ('stout', 'Stout'), ('pilsner', 'Pilsner'), ('light', 'Light')], max_length=256),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='wine_type',
            field=models.CharField(blank=True, choices=[('white', 'White'), ('red', 'Red'), ('sparkling', 'Sparkling')], max_length=256),
        ),
    ]
