# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-16 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0016_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
