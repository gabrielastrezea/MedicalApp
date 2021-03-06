# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0003_auto_20170727_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='MedicalApp.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='MedicalApp.Patient'),
        ),
    ]
