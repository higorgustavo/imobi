from django.urls import path
from .views import *


urlpatterns = [
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
]
