from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import consultar_datos


urlpatterns = [
    path('consultas/', consultar_datos, name='consultar_datos'),
]       