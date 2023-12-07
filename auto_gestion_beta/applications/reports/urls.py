from django.urls import path
from . import views
from .views import *
from django.views.generic import TemplateView

app_name = "reportes"

urlpatterns = [
    #path('generar_consulta/', generar_consulta, name='generar_consulta'),
    #path('vista-de-prueba/', consulta_view, name='prueba'),
    path('columnas/', columnas_view, name='column_Selection'),
    path('filter/', filtro_view, name='filter_Selection'),
    path('consula/', consulta_view, name='consult'),
]