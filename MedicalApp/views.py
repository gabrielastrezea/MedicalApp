# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from MedicalApp import models, forms

# Create your views here.


def list_of_medicines(request):
    medicines = models.Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'list_of_medicines.html', context)


def list_of_doctors(request):
    doctors = models.Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'list_of_doctors.html', context)


def list_of_patients(request):
    patients = models.Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'list_of_patients.html', context)


def add_medicine(request, medicine_pk=None):
    if medicine_pk:
        medicine = get_object_or_404(models.Medicine, pk=medicine_pk)
        template = 'edit_medicine.html'
    else:
        medicine = None
        template = 'add_medicine.html'

    if request.method == 'POST':
        form = forms.MedicineForm(request.POST)
        if form.is_valid():
            medicine_name = form.cleaned_data['name']
            if not medicine_pk:
                medicine = models.Medicine(name=medicine_name)
                medicine.save()
            else:
                models.Medicine.objects.filter(
                    pk=medicine_pk).update(name=medicine_name)
            return redirect('list_of_medicines')
    else:
        form = forms.MedicineForm()

    return render(request, template, {'medicine': medicine, 'form': form})


def add_doctor(request):
    if request.method == "POST":
        form = forms.DoctorForm(request.POST)
        if form.is_valid():
            if (form.data['username'] is not None and
                    form.data['password'] is not None):
                user = User(form.cleaned_data[
                            'username'], form.cleaned_data['password'])
            else:
                user = User.objects.get(pk=form.cleaned_data['user'])
            doctor = models.Doctor(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                cnp=form.cleaned_data['cnp']
            )
            doctor.save()
            return redirect('list_of_doctors')
    else:
        form = forms.DoctorForm()

    return render(request, 'add_doctor.html', {'form': form})


def login_view(request):
    context = {}
    if request.method == 'GET':
        form = forms.LoginForm()
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('list_of_medicines')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')
