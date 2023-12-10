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

def login(request):
    return render(request, "welcome/login.html")

def register(request):
    user_form = CreateUserForm
    patient_form = NewPatient


    #if request.method == 'POST':
        #user_form = CreateUserForm(request.POST)
        #patient_form = NewPatient(request.POST)
        #if form.is_valid():
            #form.save()
            #messages.success(request, 'Rejestracja przebiegła poprawnie!')
            #return redirect('register')
    
    return render(request, "welcome/register.html", {
        "user_form": user_form,
        "patient_form": patient_form
    })
    
