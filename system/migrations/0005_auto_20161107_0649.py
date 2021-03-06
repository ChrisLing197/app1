# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-07 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20161030_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='patients',
        ),
        migrations.AddField(
            model_name='registration',
            name='hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='system.Hospital'),
        ),
        migrations.AddField(
            model_name='registration',
            name='in_hospital',
            field=models.BooleanField(default=False),
        ),
    ]
