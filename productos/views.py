from django.shortcuts import render, redirect
from django.urls import reverse
from productos.models import *
from productos.forms import *

def listar_juegos(request):
    contexto = {
        "juegos" : listar_juegos.objects.all()
    }
    http_response = render(
    request=request,
    template_name="productos/juegos.html",
    context=contexto,
    )
    return http_response

def listar_hardware(request):
    contexto = {
        "Hardware" : Hardware.objects.all()
    }
    http_response = render(
    request=request,
    template_name="productos/hardware.html",
    context=contexto,
    )
    return http_response

def add_juego(request):
   if request.method == "POST":
       formulario1 = JuegosFormulario(request.POST)

       if formulario1.is_valid():
           data = formulario1.cleaned_data
           titulo = data["titulo"]
           consola = data["consola"]
           edad_recomendada = data["edad_recomendada"]
           codigo = data["codigo"]
           Juego_s = Juegos(titulo=titulo, consola=consola, edad_recomendada=edad_recomendada, codigo=codigo)
           juego.save()

           url_exitosa = reverse("listar_juegos")
           return redirect(url_exitosa)
   else:
       formulario1 = JuegosFormulario()
   
   http_response = render(
    request=request,
    template_name="productos/formulario_juegos.html",
    context={"formulario1": formulario1}
   )
   return http_response

def add_hardware(request):
   if request.method == "POST":
       formulario2 = HardwareFormulario(request.POST)

       if formulario2.is_valid():
           data = formulario2.cleaned_data
           nombre_hardware = data["nombre_hardware"]
           consola = data["consola"]
           tipo_hardware = data["tipo-hardware"]
           hardware = Hardware(nombre_hardware=nombre_hardware, consola=consola, tipo_hardware=tipo_hardware)
           hardware.save()

           url_exitosa = reverse("listar_hardware")
           return redirect(url_exitosa)
   else:
       formulario2 = HardwareFormulario()
   
   http_response = render(
    request=request,
    template_name="productos/formulario_hardware.html",
    context={"formulario2": formulario2}
   )
   return http_response

def buscar_juego(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        juegos = Juegos.objects.filter(titulo__contains=busqueda)
        contexto = {
            "juegos": juegos,
        }
        http_response = render(
            request=request,
            template_name="productos/juegos.html",
            context=contexto,
        )
        return http_response

def buscar_hardware(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        hardware = Hardware.objects.filter(titulo__contains=busqueda)
        contexto = {
            "hardware": hardware,
        }
        http_response = render(
            request=request,
            template_name='productos/hardware.html',
            context=contexto,
        )
        return http_response