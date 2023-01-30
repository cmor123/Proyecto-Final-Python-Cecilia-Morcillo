from django import forms

class DestinoFormulario(forms.Form):
    pais = forms.CharField(max_length=30)
    ciudad = forms.CharField(max_length=30)

class HospedajeFormulario(forms.Form):
    Tipo_Hospedaje= forms.CharField(max_length=30)
    Zona= forms.CharField(max_length=30)
    Cantidad_Personas= forms.IntegerField()
    
class Alquiler_CochesFormulario(forms.Form):
    Alta_Gama= forms.CharField(max_length=60)
    Media_Gama= forms.CharField(max_length=60)
    Compacto= forms.CharField(max_length=60)

class Opiniones_ViajerosFormulario(forms.Form):
     Nombre =  forms.CharField(max_length=30)
     Nacionalidad = forms.CharField(max_length=40)
     Opiniones = forms.CharField(max_length=60)

    
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
  
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']


