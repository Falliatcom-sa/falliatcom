# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-02 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0050_using_results_framework_three_options'),
        ('indicators', '0067_shorten_template_name_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leveltiertemplate',
            options={'verbose_name': 'Level tier templates'},
        ),
        migrations.AddField(
            model_name='leveltiertemplate',
            name='names',
            field=django_mysql.models.ListCharField(models.CharField(max_length=75), default=None, max_length=490, size=6),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='leveltiertemplate',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='leveltiertemplate',
            name='name',
        ),
        migrations.RemoveField(
            model_name='leveltiertemplate',
            name='tier_depth',
        ),
    ]
