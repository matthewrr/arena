# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-22 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0049_auto_20180322_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='gluten_free',
            field=models.CharField(choices=[('none', 'None'), ('gluten_free', 'Gluten-Free'), ('gluten_free_option', 'Gluten-Free Option')], default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='food',
            name='vegetarian',
            field=models.CharField(choices=[('none', 'None'), ('vegetarian', 'Vegetarian'), ('vegetarian_option', 'Vegetarian Option')], default='', max_length=256),
        ),
    ]