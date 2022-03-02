from django.urls import path
from.import views 

urlpatterns = [
    path('registro/',views.registro, name='registro'),
    path('registro/guardado',views.registroGuardado, name='registroCompleto'),
    path('solicitud/',views.solicitud, name='solicitud'),
    path('solicitud/guardada',views.solicitudGuardada, name='solicitudGuardada'),
    path('visualizacion/',views.visualizacion, name='visualizacion'),
    path('visualizacion/cambiado/<int:id>',views.cambiarEstado, name='cambiarEstado'),
    path('visualizacion/historial/', views.historialSolicitudes, name='historialSolicitudes'),
    path('calendario/',views.calendario,name='calendario'),
    path('firebase-messaging-sw.js',views.showFirebaseJS,name="show_firebase_js"),
    
]
