# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import models
from django.contrib import admin

# Register your models here.

admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Medicine)
admin.site.register(models.DosingInterval)
admin.site.register(models.MedicineAdministration)
admin.site.register(models.Prescription)
