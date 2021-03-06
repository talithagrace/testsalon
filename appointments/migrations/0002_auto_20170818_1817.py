# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='week_commencing',
            field=models.DateField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='availability',
            unique_together=set([('week_day', 'time', 'week_commencing')]),
        ),
    ]
