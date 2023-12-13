from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Patient, Meetings
from django import forms
from django.forms import ModelForm
from .forms import NewPatient, NewMeeting
from django.utils import timezone, dateformat, datetime_safe



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
        form = NewPatient(request.POST)
        if form.is_valid():
            user = form.save()
            patient = Patient.objects.create(user=user)
            group = Group.objects.get(name='patients')
            user.groups.add(group)
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

def dashboard(request):

    now = timezone.now()

    upcoming_meetings = Meetings.objects.all().filter(start_time__date=now.date())
    next_meetings = Meetings.objects.all().filter(start_time__gte=now).exclude(start_time__date=now)

    print(next_meetings)
    return render(request, "patients/dashboard.html", {
        "upcoming_meetings": upcoming_meetings,
        "next_meetings": next_meetings
    })

def meeting(request, pk):

    #przerwałem bo nie mam jeszcze logowania użytkowników a tą podstrone chciałbym filtrować po lekarzu który akurat się zaloguje

    meeting = Meetings.objects.get(id=pk)
    
    return render(request,"patients/meeting.html", {
        "meeting": meeting
    })
