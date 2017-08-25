# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=256)
    cnp = models.DecimalField(max_digits=13, decimal_places=0)

    def __unicode__(self):
        return "Doctor " + self.last_name + " " + self.first_name


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField(max_length=256)
    cnp = models.DecimalField(max_digits=13, decimal_places=0)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    street_name = models.CharField(max_length=200)
    street_number = models.DecimalField(max_digits=5, decimal_places=0)
    block = models.CharField(max_length=20)
    appartment = models.DecimalField(max_digits=4, decimal_places=0)
    postal_code = models.DecimalField(max_digits=5, decimal_places=0)
    doctor = models.ForeignKey(Doctor, null=True, related_name="patient")

    def __unicode__(self):
        return "Patient " + self.last_name + " " + self.first_name


class Medicine(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "Medicine " + self.name


class DosingInterval(models.Model):
    time = models.TimeField(null=True)
    quantity = models.DecimalField(max_digits=1, decimal_places=0)

    def __unicode__(self):
        return "Dosing " + self.pk


class MedicineAdministration(models.Model):
    medicine = models.ForeignKey(
        Medicine, related_name='medicineAdministration')
    total_quantity = models.DecimalField(max_digits=3, decimal_places=0)
    intervals = models.ForeignKey(
        DosingInterval, related_name="medicineAdministration")

    def __unicode__(self):
        return "Medicine Administration " + self.pk


class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="prescription")
    patient = models.ForeignKey(Patient, related_name="prescription")
    administration = models.ForeignKey(
        MedicineAdministration, related_name="prescription")

    def __unicode__(self):
        return "Prescription " + self.pk


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name="appointment")
    time = models.TimeField(null=True)
