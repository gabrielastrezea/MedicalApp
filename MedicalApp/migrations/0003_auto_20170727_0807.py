# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalApp', '0002_auto_20170608_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosinginterval',
            name='date',
        ),
        migrations.AddField(
            model_name='dosinginterval',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
