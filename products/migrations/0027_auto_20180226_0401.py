# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-26 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20180226_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='new_diet',
            field=models.CharField(default='', max_length=200),
        ),
    ]
