# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-18 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180217_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
