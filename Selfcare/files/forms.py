from dal import autocomplete

from django import forms

from patients.models import User


class SearchForm(forms.ModelForm):
    username = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(url='user-autocomplete')
    )
    class Meta:
        model = User
        fields = ('username',)