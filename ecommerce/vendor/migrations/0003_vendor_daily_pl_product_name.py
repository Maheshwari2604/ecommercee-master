# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-02 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendor_daily_pl'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_daily_pl',
            name='product_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
