# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 20:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('email', models.EmailField(max_length=256)),
                ('cnp', models.DecimalField(decimal_places=0, max_digits=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DosingInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineAdministration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('intervals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicineAdministration', to='MedicalApp.DosingInterval')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicineAdministration', to='MedicalApp.Medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('email', models.EmailField(max_length=256)),
                ('cnp', models.DecimalField(decimal_places=0, max_digits=13)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=200)),
                ('street_name', models.CharField(max_length=200)),
                ('street_number', models.DecimalField(decimal_places=0, max_digits=5)),
                ('block', models.CharField(max_length=20)),
                ('appartment', models.DecimalField(decimal_places=0, max_digits=4)),
                ('postal_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='MedicalApp.MedicineAdministration')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='MedicalApp.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='MedicalApp.Patient')),
            ],
        ),
    ]
