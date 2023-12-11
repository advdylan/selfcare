from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from patients.models import Doctor, Patient, Meetings
from django import forms
from django.forms import ModelForm
from patients.forms import NewPatient, NewMeeting
from django.utils import timezone, dateformat, datetime_safe
from .forms import CreateUserForm

# Create your views here.

def index(request):
    return render(request, "welcome/index.html")

def register(request):
    user_form = CreateUserForm
    patient_form = NewPatient


    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        patient_form = NewPatient(request.POST)
        if user_form.is_valid() and patient_form.is_valid():

            user = user_form.save()
            patient = patient_form
            patient = patient_form.save(commit=False)

            patient.first_name = user_form.cleaned_data.get('first_name')
            patient.last_name = user_form.cleaned_data.get('last_name')
            patient.email = user_form.cleaned_data.get('email')     
            patient.save()

            messages.success(request, 'Rejestracja przebiegła poprawnie!')
            return redirect('register')
    else:
        user_form = CreateUserForm()
        patient_form = NewPatient()
    
    return render(request, "welcome/register.html", {
        "user_form": user_form,
        "patient_form": patient_form
    })
    
