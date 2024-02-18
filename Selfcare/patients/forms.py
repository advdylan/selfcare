from django.forms import ModelForm, MultiValueField, FileInput, MultiWidget
from django import forms
from .models import Doctor,Patient,Meetings, Image, Document, User



#calendar custom widget

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class NewPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'street','code','city', 'phone_number', 'curator', 'email',)


        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'street': 'Ulica i numer domu',
            'code': 'Kod pocztowy',
            'city': 'Miejscowość',
            'phone_number': 'Numer telefonu',
            'curator': 'Wybierz lekarza prowadzącego',
            'email': 'Adres e-mail'
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
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
            'start_time': DateTimeInput(attrs={'class': 'form-select'}, format='%d-%m-%Y, %H:%M'),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'patient': forms.Select(attrs={'class': 'form-select'})
        }


class NewDoctor(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'street','code','city', 'phone_number', 'proteges', 'email',)


        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'street': 'Ulica i numer domu',
            'code': 'Kod pocztowy',
            'city': 'Miejscowość',
            'phone_number': 'Numer telefonu',
            'proteges': 'Wybierz pacjentów',
            'email': 'Adres e-mail'
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'proteges': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'})
        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file',}))

    class Meta:
        model = Image
        fields = ('image', )

class DocumentForm(forms.ModelForm):
    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file',}))

    data = User.objects.all()
    user_names = [(user.first_name + ' ' + user.last_name, user.username) for user in data]



    allowed_users = forms.ModelMultipleChoiceField(queryset=user_names, widget=forms.SelectMultiple(attrs={'class': 'form-control', }))
    class Meta:
        model = Document
        fields = ('document', 'allowed_users',)
        labels = {
            'Document': 'Dokument',
            'allowed_users': 'Udostępnij'
        }
