from .models import Doctor, Patient, Meetings, Document, Image, User
from django.contrib import messages
import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from django.views import View
from patients.models import User


import re



def extract(request, description):
    
    pattern = r'http://127\.0\.0\.1:8000/patients/(doctor|patient)/(\d+)'

    # Find matches
    matches = re.findall(pattern, description)
   
    # Print matches
    doctor_id = 0
    patient_id = 0
    for match in matches:
        
        if match[0] == 'doctor':
            doctor_id = match[1]
            #print(doctor_id)
        elif match[0] == 'patient':
            patient_id = match[1]
            #print(patient_id)

    doctor = Doctor.objects.get(id = doctor_id)
    patient = Patient.objects.get(id = patient_id)
    return doctor, patient
""""
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
    """


""""
#def get_doctor_id(request, doctor):

    try:
        person = Doctor.objects.get(doctor=doctor)
        doctor_id = person.id
    except Doctor.DoesNotExist:
        messages.error(request, f'Nie znaleziono lekarza {doctor} w bazie danych')
        return redirect('calendar')
    return doctor_id

#def get_patient_id(request, patient):

    try:
        person = Patient.objects.get(patient=patient)
        patient_id = person.id
    except Patient.DoesNotExist:
        messages.error(request, f'Nie znaleziono lekarza {patient} w bazie danych')
        return redirect('calendar')
    return patient_id
    """

def group_required(group, login_url=None, raise_exception=False):
    """
    Decorator for views that checks whether a user has a group permission,
    redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        # First check if the user has the permission (even anon users)

        if user.groups.filter(name__in=groups).exists():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url=login_url)

def add_permission(request):

    if request.method == "POST":
        data = request.POST
        print(f"POST DATA: {data}")
        try:       
            username = request.POST['username']
            user = get_user_by_username(username)
            if user is None:
                messages.error(request, 'Brak użytkownika o podanej nazwie!')
            else:
                document = get_object_or_404(Document, id= request.POST['docId'])
                if document is None:
                    messages.error(request, 'Błąd dokumentu')
                else:
                    document.allowed_users.add(user)
                    messages.success(request, f'Udostępniono poprawnie dla uzytkownika {user}')


        except Exception as e:
            print(f"Error in add_permission: {e}")
        else:
            return redirect('upload_images')
        return redirect('upload_images')
    
    

def get_user_by_username(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        pass

    try:
        return Patient.objects.get(user__username=username)
    except Patient.DoesNotExist:
        pass

    try:
        return Doctor.objects.get(user__username=username)
    except Doctor.DoesNotExist:
        pass

    return None


class UserAutoComplete(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        users = User.objects.filter(username__icontains=query)
        user_list = [user.username for user in users]
        return JsonResponse(user_list, safe=False)
    
