from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Patient, Meetings
from django import forms
from django.forms import ModelForm
from .forms import NewPatient, NewMeeting


# Create your views here.

def index(request):
    return render(request, "patients/index.html")

def meetings(request):

    meetings = Meetings.objects.all()

    #update the status of meeting
    for meeting in meetings:
        meeting.status()
        meeting.save()
        
    return render(request, "patients/meetings.html", {
        "meetings": meetings
    })

def patients(request):

    patients = Patient.objects.all()
    
    return render(request,"patients/patients.html", {
        "patients": patients
    })

def patient(request, pk):

    patient = Patient.objects.get(id=pk)
    meeting = Meetings.objects.filter(patient=patient)
   
    return render(request,"patients/patient.html", {
        "patient": patient,
        "meeting": meeting
    })

def newpatient(request):
    
    form = NewPatient

    if request.method == 'POST':
        print(request.POST)
        form = NewPatient(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pacjent dodany poprawnie!')
            return redirect('newpatient')


    return render(request, "patients/newpatient.html",{
        "form": form
    })

def newmeeting(request):
    form = NewMeeting
    
    if request.method == 'POST':
        print(request.POST)
        form = NewMeeting(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Spotkanie dodane poprawnie!')

    return render(request, "patients/newmeeting.html", {
        "form": form
    })