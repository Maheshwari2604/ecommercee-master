# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-02-05 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Loma', '0030_remove_md_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='md',
            name='loma_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Loma.Loma_master'),
        ),
    ]
