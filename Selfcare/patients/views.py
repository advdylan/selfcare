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

