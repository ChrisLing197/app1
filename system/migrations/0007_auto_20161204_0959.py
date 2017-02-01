# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-04 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20161118_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='record',
        ),
        migrations.RemoveField(
            model_name='record',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='employed_hospitals',
        ),
        migrations.AddField(
            model_name='registration',
            name='employed_hospital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='system.Hospital'),
        ),
        migrations.AlterField(
            model_name='record',
            name='record_type',
            field=models.CharField(choices=[('DG', 'Diagnosis'), ('TR', 'Test Results'), ('HR', 'Hospital Record'), ('SY', 'Symptoms'), ('RX', 'Prescription')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
    ]