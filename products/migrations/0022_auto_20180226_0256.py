# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-26 02:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20180222_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='alcohol_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='alt_v',
        ),
        migrations.RemoveField(
            model_name='product',
            name='beverage_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='course',
        ),
        migrations.RemoveField(
            model_name='product',
            name='diet',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gf',
        ),
        migrations.RemoveField(
            model_name='product',
            name='serving_type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='v',
        ),
    ]
