from django.contrib import admin
from .models import Rol, EstadoCivil, Municipio, Direccion, Persona, Pregunta, Usuario

# Register your models here.

admin.site.register(Rol)
admin.site.register(EstadoCivil)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(Persona)
admin.site.register(Pregunta)
admin.site.register(Usuario)