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
        return redirect('calendar')
    except Patient.DoesNotExist:
        messages.error(request, f'Nie znaleziono pacjenta {patient_first_name} {patient_last_name} w bazie danych')
        return redirect('calendar')

    return doctor, patient


    
def get_doctor_id(request, doctor):

    try:
        person = Doctor.objects.get(doctor=doctor)
        doctor_id = person.id
    except Doctor.DoesNotExist:
        messages.error(request, f'Nie znaleziono lekarza {doctor} w bazie danych')
        return redirect('calendar')
    return doctor_id

def get_patient_id(request, patient):

    try:
        person = Patient.objects.get(patient=patient)
        patient_id = person.id
    except Patient.DoesNotExist:
        messages.error(request, f'Nie znaleziono lekarza {patient} w bazie danych')
        return redirect('calendar')
    return patient_id


    