from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Usuario123'}), max_length=30,
        required=True, help_text='Requerido. 30 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Contraseña123'}), max_length=30, required=True,
        help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(
        label='Repetir Password', widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Contraseña123'}), max_length=30, required=True,
        help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')
    first_name = forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'nombre form-control', 'placeholder': 'Mario'}), max_length=30,
        required=True, help_text='Solo debe contener letras')
    last_name = forms.CharField(
        label='Apellido', widget=forms.TextInput(attrs={'class': 'apellido form-control', 'placeholder': 'Diaz'}), max_length=30,
        required=True, help_text='Solo debe contener letras')
    email = forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email form-control', 'placeholder': 'micorreo@correo.com'}), max_length=254,
        required=True, help_text='Se requiere una direccion de email valida.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
