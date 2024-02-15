from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from patients.models import Doctor, Patient, Meetings, Image, Document
from django.utils import timezone
from datetime import datetime
from django import forms
from django.forms import ModelForm, inlineformset_factory
from patients.forms import NewPatient, NewMeeting, NewDoctor, ImageForm, DocumentForm
from patients.helpers import extract, group_required, testUserAutoComplete

from django.http import JsonResponse
from django.views import generic

from decouple import config



def index(request):
     pass

@group_required('doctors')
def notes(request):
    return render(request, "patients/notes.html")


@group_required('doctors')
def upload_images(request):
    users = User.objects.all()
    owned_document = Document.objects.filter(user=request.user)
    received_document = Document.objects.filter(allowed_users = request.user).exclude(user=request.user)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            form.save()
    else:
            image_form = ImageForm()
            file_form = DocumentForm()

    images = Image.objects.filter(user = request.user)      
    return render(request, "files/notes.html", {
            'image_form': image_form,
            'file_form': file_form,
            'images': images,
            'owned_document': owned_document,
            'received_document': received_document,
            'users': users,
        } )

@group_required('doctors')
def upload_files(request):


    try:
        if request.method == "POST":
            form = DocumentForm(request.POST, request.FILES)
            now = timezone.now()
            
            if form.is_valid():
                data = request.POST
                print(f"POST DATA: {data}")
                document = form.save(commit=False)
                document.user = request.user
                document.name = request.FILES['document']
                document.date = now
                document.save()
                allowed_users = request.POST.getlist('allowed_users') 
                document.allowed_users.set(allowed_users)
            
        else:
            file_form = DocumentForm()

    
    except Exception as e:
            print(f"Error: {e}")
            
    return redirect('upload_images')

def autocomplete_user(request):
    query = request.GET.get('q')
    results = User.objects.filter(username__icontains=query)[:10]
    data = [{'pk': user.pk, 'value': user.username} for user in results]
    return JsonResponse({'results': data})