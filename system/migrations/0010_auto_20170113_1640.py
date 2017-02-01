# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-13 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20170113_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='employed_hospital',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='in_hospital',
        ),
        migrations.AlterField(
            model_name='record',
            name='record_type',
            field=models.CharField(choices=[('DG', 'Diagnosis'), ('TR', 'Test Results'), ('SY', 'Symptoms'), ('RX', 'Prescription')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
    ]