# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-27 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0031_organization_sectors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(default='TolaData', max_length=255, verbose_name='Organization Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='primary_address',
            field=models.CharField(max_length=255, null=True, verbose_name='Primary Address'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='primary_contact_email',
            field=models.CharField(max_length=255, null=True, verbose_name='Primary Contact Email'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='primary_contact_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Primary Contact Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='primary_contact_phone',
            field=models.CharField(max_length=255, null=True, verbose_name='Primary Contact Phone'),
        ),
    ]
