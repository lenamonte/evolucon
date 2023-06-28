from django import forms
from django.contrib.auth.models import User
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nome', 'cpf',)
        
        
        

class RegistroForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)