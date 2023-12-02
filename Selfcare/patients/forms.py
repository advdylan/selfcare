from django.forms import ModelForm
from django import forms
from .models import Doctor,Patient,Meetings

class NewPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'curator', 'email')


        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'address': 'Adres',
            'phone_number': 'Numer telefonu',
            'curator': 'Wybierz lekarza prowadzącego',
            'email': 'Adres e-mail'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'label': 'OK'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'curator': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'})
        }

class NewMeeting(forms.ModelForm):
    class Meta:
        model = Meetings
        fields = ('meeting_place', 'start_time', 'doctor', 'patient',)

        labels = {
            'meeting_place': 'Rodzaj spotkania',
            'start_time': 'Data rozpoczęcia',
            'doctor': 'Terapeuta',
            'patient': 'Pacjent'
        }

        widgets = {
            'meeting_place': forms.Select(attrs={'class': 'form-select'}),
            'start_time': forms.DateField(atts={'class': 'form-control'}),
            'doctor': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'patient': forms.SelectMultiple(attrs={'class': 'form-select'})
        }

