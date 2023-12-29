from .models import Doctor, Patient, Meetings
from django.contrib import messages
from django.shortcuts import render, redirect

def extract(request, description):
    doctor_label, patient_label = description.split('. ')

    _, doctor_fullname = doctor_label.split(': ')
    doctor_first_name, doctor_last_name = doctor_fullname.split(' ')

    _, patient_fullname = patient_label.split(': ')
    patient_first_name, patient_last_name = patient_fullname.split(' ')

    #print(doctor_first_name, doctor_last_name, patient_first_name, patient_last_name)

    doctor = Doctor.objects.filter(first_name = doctor_first_name, last_name = doctor_last_name)
    patient = Patient.objects.filter(first_name = patient_first_name, last_name = patient_last_name)
    if doctor.exists() and patient.exists:
        return doctor, patient
    
    else:
        messages.error(request, 'Nie znaleziono pacjenta lub lekarza w bazie danych')
        return redirect('your_view_name')

    


    