# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20170820_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='style',
            new_name='styles',
        ),
    ]