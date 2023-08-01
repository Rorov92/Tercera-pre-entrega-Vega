from django.contrib import admin
from django.urls import path
from productos.views import *

urlpatterns = [
    path("juegos/", listar_juegos, name="listar_juegos"),
    path("hardware/", listar_hardware, name="listar_hardware"),
    path("agregarjuegos/", add_juego, name="agregar_juegos"),
    path("agregarhardware/", add_hardware, name="agregar_hardware"),
    path("buscarjuego/", buscar_juego, name="buscar_juego"),
    path("buscarhardware/", buscar_hardware, name="buscar_hardware"),
    ]