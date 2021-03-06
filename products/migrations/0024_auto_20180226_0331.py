# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-26 03:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_beverage_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='gf',
            new_name='gluten_free',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='v',
            new_name='vegetarian',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='alt_v',
            new_name='vegetarian_optional',
        ),
        migrations.AddField(
            model_name='beverage',
            name='abv',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='beverage',
            name='company',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='beverage',
            name='company_location',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='beverage',
            name='ibu',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='food',
            name='gluten_free_optional',
            field=models.BooleanField(default=False),
        ),
    ]
