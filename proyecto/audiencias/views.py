import json
from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from .models import *
from .forms import *
# Create your views here.

def registro(request):
    formulario=AudienciaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registroCompleto')
    return render(request, 'registroAudiencia.html',{'form':AudienciaForm})

def registroGuardado(request):
    formulario=AudienciaForm(request.POST or None, request.FILES or None)
    return render(request, 'registroAudiencia.html',{'form':AudienciaForm,'validacion':'OK'})


def solicitud(request):
    formulario=SolicitudAudienciaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        
        formulario.save()
        #resgistration  = ['AAAA8tucvcc:APA91bGpuq-fc85yFJVxoSG2UylCjpy2HF_KPfaTa1qxUm3KdKVsPRwliI5p0mEdfYn30QHp5hAWGk3p2Wd-aeS2qbuM9MHbPBrYnJgS-70HZk09Ke_UTdRZvRcH5PWwP_2YT5QvFWlG']
        #send_notification(resgistration , 'Nueva solicitud ingresada' , 'Se a ingreasdo una nueva solicitud de audiencia')
        return redirect('solicitudGuardada')
    return render(request, 'solicitudAudiencia.html',{'formSolicitud':SolicitudAudienciaForm})

def solicitudGuardada(request):
    formulario=SolicitudAudienciaForm(request.POST or None, request.FILES or None)
    return render(request, 'solicitudAudiencia.html',{'formSolicitud':SolicitudAudienciaForm,'validacion':'OK'})


def cambiarEstado(request,id):
    solicitud= SolicitudAudiencia.objects.get(id=id)
    formulario=CambiarEstadoForm(request.POST)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('historialSolicitudes')
    return render(request,'cambiarEstadoSolicitud.html',{'formEstado':CambiarEstadoForm})

def visualizacion(request):
    solicitudes= SolicitudAudiencia.objects.all()
    return render(request, 'audiencias.html',{'solicitudes':solicitudes})

def historialSolicitudes(request):
    solicitudes= SolicitudAudiencia.objects.all()
    return render(request, 'historialSolicitudes.html',{'solicitudes':solicitudes})

def calendario(request):
    audiencias= Audiencia.objects.all()
    return render(request, 'calendar.html',{'audiencias':audiencias})
#notificacion

def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAA8tucvcc:APA91bGpuq-fc85yFJVxoSG2UylCjpy2HF_KPfaTa1qxUm3KdKVsPRwliI5p0mEdfYn30QHp5hAWGk3p2Wd-aeS2qbuM9MHbPBrYnJgS-70HZk09Ke_UTdRZvRcH5PWwP_2YT5QvFWlG	"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload))
    print(result.json())


def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyClPLGmQD7F3IoaB9PDcMLMAU4_g0B4gJQ",' \
         '        authDomain: "proyectoaudiencias-cdb5a.firebaseapp.com",' \
         '        databaseURL: "https://proyectoaudiencias-cdb5a-default-rtdb.firebaseio.com/",' \
         '        projectId: "proyectoaudiencias-cdb5a",' \
         '        storageBucket: "proyectoaudiencias-cdb5a.appspot.com",' \
         '        messagingSenderId: "1043066568135",' \
         '        appId: "1:1043066568135:web:2fbd95c353eab9f6fc2de2",' \
         '        measurementId: "G-GHJ78G9YFL"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")


    
