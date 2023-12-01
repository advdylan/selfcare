from django.forms import ModelForm
from .models import Doctor,Patient,Meetings

class NewPatient(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

