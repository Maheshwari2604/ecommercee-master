# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 12:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0010_auto_20190203_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approved_pl_by_loma',
            old_name='list_price',
            new_name='cal_offer_price',
        ),
        migrations.RemoveField(
            model_name='approved_pl_by_loma',
            name='offer_price',
        ),
        migrations.RemoveField(
            model_name='approved_pl_by_loma',
            name='vendor_id',
        ),
    ]