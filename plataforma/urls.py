from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('imovel/<str:id>', detalhar_imovel, name='detalhar_imovel'),
    path('agendar_visitas', agendar_visitas, name="agendar_visitas"),
    path('agendamentos', agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', cancelar_agendamento, name="cancelar_agendamento"),
]
