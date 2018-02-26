# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-22 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180221_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.BooleanField(default=False),
        ),
    ]