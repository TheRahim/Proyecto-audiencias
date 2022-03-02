from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Juez)
admin.site.register(Materia)
admin.site.register(Rit)
admin.site.register(Audiencia)
admin.site.register(SolicitudAudiencia)
admin.site.register(UnidadRevision)
admin.site.register(Estadistica)
admin.site.register(RevisionPost)