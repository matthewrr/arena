# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-13 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_stand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='products.Genre'),
        ),
    ]
