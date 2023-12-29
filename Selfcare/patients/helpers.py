from .models import Doctor, Patient, Meetings
from django.contrib import messages
from django.shortcuts import render, redirect

def extract(request, description):
    doctor_label, patient_label = description.split('. ')

    _, doctor_fullname = doctor_label.split(': ')
    doctor_first_name, doctor_last_name = doctor_fullname.split(' ')

    _, patient_fullname = patient_label.split(': ')
    patient_first_name, patient_last_name = patient_fullname.split(' ')

    try:
        doctor = Doctor.objects.get(first_name=doctor_first_name, last_name=doctor_last_name)
        patient = Patient.objects.get(first_name=patient_first_name, last_name=patient_last_name)
    except Doctor.DoesNotExist:
        messages.error(request, f'Nie znaleziono lekarza {doctor_first_name} {doctor_last_name} w bazie danych')
        return redirect('your_view_name')
    except Patient.DoesNotExist:
        messages.error(request, f'Nie znaleziono pacjenta {patient_first_name} {patient_last_name} w bazie danych')
        return redirect('your_view_name')

    return doctor, patient


    


    