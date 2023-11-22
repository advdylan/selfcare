from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "patients/index.html")

def meetings(request):
    return render(request, "patients/meetings.html", {
        ""
    } )