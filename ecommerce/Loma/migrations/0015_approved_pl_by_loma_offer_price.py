# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-03 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0014_approved_pl_by_loma_list_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='approved_pl_by_loma',
            name='offer_price',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
