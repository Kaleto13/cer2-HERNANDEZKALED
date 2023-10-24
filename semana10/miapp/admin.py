from django.contrib import admin
from miapp.models import *
from django.contrib.auth.models import Permission


# Register your models here.

admin.site.register(Comunicado)
admin.site.register(Entidades)
admin.site.register(Administrador_Entidad)


