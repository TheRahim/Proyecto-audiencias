from email.policy import default
from django import forms

class ContactForm(forms.Form):
    correo_institucional = forms.EmailField(required=True)
    contrasena= forms.CharField( required=True)

class ContrasenaForm(forms.Form):
    correo_institucional= forms.EmailField(required=True)