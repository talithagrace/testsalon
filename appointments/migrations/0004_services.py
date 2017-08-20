# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20170818_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price starts from: ')),
            ],
        ),
    ]
