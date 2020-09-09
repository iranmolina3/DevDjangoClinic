from django.urls import path
from .views import *

urlpatterns = [
    path('create_persona/', create_persona, name = 'create_persona'),
    path('read_persona/', read_persona, name = 'read_persona'),
    path('update_persona/<int:pk_persona>', update_persona, name = 'update_persona'),
    path('delete_persona/<int:pk_persona>', delete_persona, name = 'delete_persona'),

    path('create_consulta/', create_consulta, name = 'create_consulta'),
    path('read_consulta/', read_consulta, name = 'read_consulta'),
    path('update_consulta/<int:pk_consulta>', update_consulta, name = 'update_consulta'),
    path('delete_consulta/<int:pk_consulta>', delete_consulta, name = 'delete_consulta'),

    path('create_examen_fisico/', create_examen_fisico, name = 'create_examen_fisico'),
    path('listar_examen_fisico', read_examen_fisico, name = 'read_examen_fisico'),
]