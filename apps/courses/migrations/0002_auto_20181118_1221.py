# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-11-18 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='students',
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u7ea7'), ('\uff47j', '\u9ad8\u7ea7')], max_length=2, verbose_name='\u96be\u5ea6'),
        ),
    ]
