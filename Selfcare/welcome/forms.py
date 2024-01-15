from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    """"
    token = forms.CharField(
        widget=forms.HiddenInput()
    )
    """
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2', ]

        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'username': 'Nazwa użytkownika',
            'email': 'Adres e-mail',
            'password1': 'Hasło',
            'password2': 'Powtórz hasło'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'password1': forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password','required': 'required'}, )),
            'password2': forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password','required': 'required'}, ))

        }

class LoginUserForm(forms.Form):

    fields = ['username', 'password']
    model = User
    username = forms.CharField(label='Nazwa użytkownika lub adres e-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa użytkownika lub adres e-mail'}))
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))


#class AuthForm(AuthenticationForm):
    #username = forms.EmailField(max_length=254, required=True,
                                #widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    #password = forms.CharField()