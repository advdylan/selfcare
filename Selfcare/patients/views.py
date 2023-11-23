from django.shortcuts import render
from .models import Doctor, Patient, Meetings


# Create your views here.

def index(request):
    return render(request, "patients/index.html")

def meetings(request):
    meetings = Meetings.objects.all()
    return render(request, "patients/meetings.html", {
        "meetings": meetings
    })