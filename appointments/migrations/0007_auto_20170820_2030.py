# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_auto_20170820_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price starts from (£)'),
        ),
    ]
