# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-11-18 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20181117_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='\u987a\u5e8f'),
        ),
    ]
