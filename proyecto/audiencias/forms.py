from django import forms
from tkinter import Widget
from xml.dom.minidom import Attr
from dataclasses import field, fields
from apps.models import *

class DateInput(forms.DateInput):
    input_type='date'
    
class TimeInput(forms.TimeInput):
    input_type='time'
     
class AudienciaForm(forms.ModelForm):
    class Meta:
        model= Audiencia
        fields= ('juez','tipo_audiencia','materia','rit','cant_bloques','abogado_curador','fecha_audiencia','hora_audiencia','fecha_ingreso_causa','fecha_nuevaAudiencia','notificacion_exhorto','parte_recluida','parte_santa_maria','audiencia_reservada','audiencia_interprete')
        widgets= {'fecha_audiencia': DateInput(),'hora_audiencia':TimeInput(),'fecha_ingreso_causa': DateInput(),'fecha_nuevaAudiencia':DateInput()}
        
        
class SolicitudAudienciaForm(forms.ModelForm):
    class Meta:
        model= SolicitudAudiencia
        fields= ('juez','tipo_audiencia','materia','rit','cant_bloques','abogado_curador','fecha_audiencia','hora_audiencia','notificacion_exhorto','parte_recluida','parte_santa_maria','audiencia_reservada','audiencia_interprete')
        widgets={'fecha_audiencia': DateInput(),'hora_audiencia':TimeInput()}
        
class CambiarEstadoForm(forms.ModelForm):
    class Meta:
        model= SolicitudAudiencia
        fields=('estado',)
