# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-20 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0046_auto_20180320_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='vegetarian',
            field=models.CharField(default='no', max_length=32),
        ),
    ]