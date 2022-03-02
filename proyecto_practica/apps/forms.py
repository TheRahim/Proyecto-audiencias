from socket import fromshare
from django import forms
from .models import *

class RitForm(forms.ModelForm):
    class Meta:
        model=Rit
        fields=('letra','nro_causa','anio')