from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('consulta/<str:tabla>/', views.consultar_datos, name='consultar_datos'),
    # Otras rutas de tu aplicación
    path('base/', TemplateView.as_view(template_name='base.html'), name='base_view'),
]