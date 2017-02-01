# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-13 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_auto_20170113_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient',
            new_name='buyer',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='doctor',
            new_name='seller',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='patient',
            new_name='buyer',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='patient_readable',
            new_name='buyer_readable',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='doctor',
            new_name='seller',
        ),
    ]