# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-17 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0020_auto_20170116_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='poster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_item', to='system.Registration'),
        ),
    ]
