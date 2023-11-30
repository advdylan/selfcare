from django.shortcuts import render
from .models import Doctor, Patient, Meetings


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
    
    return render(request, "patients/newpatient.html")