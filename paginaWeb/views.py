from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import tablaPruevaForm, tablaVinculadaForm
from .models import tablaPrueva
from .models import Mascota

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def ingresarTabla1(request):
    if request.method == "POST":
        form = tablaPruevaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Guardado")
    else:
        form = tablaPruevaForm()   
    return render(request, "ingresarTabla1.html", {"form": form})

def ingresarTabla2(request):
    if request.method == "POST":
        form = tablaVinculadaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Guardado")
    else:
        form = tablaVinculadaForm()   
    return render(request, "ingresarTabla1.html", {"form": form})
def verTabla1s(request):
    return render(request, "verTabla1.html", {"tablas": tablaPrueva.objects.all()})

def verTabla1Unica(request, id):
    return render(request, "verTablaUnica.html", {"tabla": tablaPrueva.objects.get(id=id).__dict__.items})

#Nuevos vistas 

#def crear_mascota():


def obtener_detalles(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    detalles=mascota.obtenerDetalles()
    return render(request,"detalles_mascota.html",{"mascota":detalles})

def actualizar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        data = request.POST
        mascota.actualizarMascota(**data.dict())  # Convierte QueryDict en diccionario
        return render(request,"actualizar_mascota.html",{"mascota":mascota,"mensaje":"Mascota actualizada correctamente"})
    return render(request,"actualizar_mascota.html",{"mascota":mascota})

def obtener_ubicacion(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    return render(request,"ubicacion_mascota.html",{"ubicacion":mascota.obtenerUbicacion()})

def actualizar_ubicacion(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == "POST":
        nueva_direccion = request.POST.get("direccion")
        if nueva_direccion:
            mensaje=mascota.actualizarUbicacion(nueva_direccion)
            return render(request,"actualizar_ubicacion.html",{"mascota":mascota,"mensaje":mensaje})
        else:
            return render(request,"actualizar_ubicacion.html",{"mascota":mascota,"error":"Falta la nueva direccion"})
    return render(request,"actualizar_ubicacion.html",{"mascota":mascota})
