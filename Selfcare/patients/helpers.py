from .models import Doctor, Patient, Meetings

def extract(description):
    parts = description.split('. ')

    doctor_fullname = parts[0].split(': ')
    doctor_split = doctor_fullname[1].split(',')
    doctor_name = doctor_split[0].split(' ')
    
    patient_fullname = parts[1].split(': ')
    patient_split = patient_fullname[1].split(',')
    patient_name = patient_split[0].split(' ')

    doctor_first_name = doctor_name[0]
    doctor_last_name = doctor_name[1]

    patient_first_name = patient_name[0]
    patient_last_name = patient_name[1]

    

    print(doctor_first_name, doctor_last_name, patient_first_name, patient_last_name)
    

    return doctor_name, patient_name