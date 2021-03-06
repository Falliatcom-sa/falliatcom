# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-13 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """Create field so that existing programs can migrate to satsuma
    
    Makes a field "workflow_program.using_results_framework" that is a boolean
        - field indicates that programs should display their indicators grouped by new RF levels
        - field is default False for all existing programs (this will be set to true in admin)
    Alters the field after all existing programs are migrated to default to True
    """

    dependencies = [
        ('workflow', '0046_fill_tolauser_username_field'),
    ]

    operations = [
        # first add the field with a default of false, so existing programs are set as "unmigrated"
        migrations.AddField(
            model_name='program',
            name='using_results_framework',
            field=models.BooleanField(default=False, verbose_name='Group indicators according to the results framework'),
        ),
        # now make the default true so all new programs going forward have this set
        # (new programs don't need migration time)
        migrations.AlterField(
            model_name='program',
            name='using_results_framework',
            field=models.BooleanField(default=True, verbose_name='Group indicators according to the results framework'),
        ),
    ]
