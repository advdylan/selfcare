from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Patient, Meetings
from django.utils import timezone
from datetime import datetime
from django import forms
from django.forms import ModelForm
from .forms import NewPatient, NewMeeting, NewDoctor



from .calendar_API import test_calendar, new_event, fetch_calendar, parse_calendar, get_settings
from .helpers import extract
from decouple import config



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

def doctors(request):

    doctors = Doctor.objects.all()
    
    return render(request,"patients/doctors.html", {
        "doctors": doctors
    })

def patient(request, pk):

    patient = Patient.objects.get(id=pk)
    meeting = Meetings.objects.filter(patient=patient)

   
    return render(request,"patients/patient.html", {
        "patient": patient,
        "meeting": meeting
    })

def doctor(request, pk):

    doctor = Doctor.objects.get(id=pk)
    meeting = Meetings.objects.filter(doctor=doctor)
   
    return render(request,"patients/doctor.html", {
        "doctor": doctor,
        "meeting": meeting
    })

def newpatient(request):
    form = NewPatient
    if request.method == 'POST':
        form = NewPatient(request.POST)
        if form.is_valid():
            user = form.save()
            #group = Group.objects.get(name='patients')
            #user.groups.add(group)
            #patient = Patient(user=user)
            #patient.save()
            messages.success(request, 'Pacjent dodany poprawnie!')
            return redirect('newpatient')


    return render(request, "patients/newpatient.html",{
        "form": form
    })

def newdoctor(request):
    form = NewDoctor
    if request.method == 'POST':
        form = NewDoctor(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='doctors')
            user.groups.add(group)
            doctor = Doctor(user=user)
            doctor.save()
            messages.success(request, 'Lekarz dodany poprawnie!')
            return redirect('newdoctor')


    return render(request, "patients/newdoctor.html",{
        "form": form
    })

def newmeeting(request):
    form = NewMeeting
    
    if request.method == 'POST':
        form = NewMeeting(request.POST)
        if form.is_valid():
            new_meeting = form.save()

            description = f'Lekarz: {new_meeting.doctor}.Pacjent: {new_meeting.patient} <a href=""'
            

            location = new_meeting.meeting_place
            start = new_meeting.start_time
            end = new_meeting.end_time
            new_event(location, description, start,end)
            messages.success(request, 'Spotkanie dodane poprawnie!')

    return render(request, "patients/newmeeting.html", {
        "form": form
    })

def dashboard(request):

    now = timezone.now()

    upcoming_meetings = Meetings.objects.all().filter(start_time__date=now.date())
    next_meetings = Meetings.objects.all().filter(start_time__gte=now).exclude(start_time__date=now)

    return render(request, "patients/dashboard.html", {
        "upcoming_meetings": upcoming_meetings,
        "next_meetings": next_meetings
    })

def meeting(request, pk):

    #przerwałem bo nie mam jeszcze logowania użytkowników a tą podstrone chciałbym filtrować po lekarzu i pacjencie który akurat się zaloguje

    meeting = Meetings.objects.get(id=pk)
    
    return render(request,"patients/meeting.html", {
        "meeting": meeting
    })

def calendar(request):
    form = NewMeeting
    #results = test_calendar()
    now = timezone.now()

    upcoming_meetings = Meetings.objects.all().filter(start_time__date=now.date())
    next_meetings = Meetings.objects.all().filter(start_time__gte=now).exclude(start_time__date=now)

    if request.method == "POST":
        form = NewMeeting(request.POST)
        if form.is_valid():
            new_meeting = form.save()

            #patient_id = get_patient_id(request, new_meeting.patient)
            #doctor_id = get_doctor_id(request, new_meeting.doctor)

            #print(patient_id, doctor_id)

            patient_url = request.build_absolute_uri(reverse('patient', args=[new_meeting.patient.id]))
            doctor_url = request.build_absolute_uri(reverse('doctor', args=[new_meeting.doctor.id]))
            
            description = f'Lekarz: <a href="{doctor_url}"> {new_meeting.doctor}</a>. Pacjent:<a href="{patient_url}">  {new_meeting.patient}</a>'
            doctor = new_meeting.doctor
            patient = new_meeting.patient
            location = new_meeting.meeting_place
            start = new_meeting.start_time
            end = new_meeting.end_time
            new_event(location, description, start, end, doctor, patient)

        return render(request,"patients/calendar.html", {
        'form': form,
        "upcoming_meetings": upcoming_meetings,
        "next_meetings": next_meetings
    })
        

    return render(request,"patients/calendar.html", {
        'form': form,
        "upcoming_meetings": upcoming_meetings,
        "next_meetings": next_meetings
    })


def synchro(request):
    #synchronizacja działa ale nie sprawdza czy w Django Database są już te spotkania z kalendarza.
    #Zalecam usunąć najpierw całe ORM albo ruszyć dupę i napisać funkcje która sprawdzi czy spotkanie jest w bazie

    #deleting the existent meetings in Django Database 
    #Meetings.objects.all().delete()

    #getting the information from Google Calendar
    events = fetch_calendar()

    #parsing the Google Calendar data and transfering it to the Django Database
    parse_calendar(request,events)
    
    return render(request, "patients/calendar.html")

def apisettings(request):
    
    get_settings()
    return redirect('calendar')

