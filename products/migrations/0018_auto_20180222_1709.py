# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-22 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20180222_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]