from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import tablaPruevaForm, tablaVinculadaForm, MascotaForm
from .forms import UsuarioForm
from .models import Usuario
from .models import tablaPrueva
from .models import Mascota

# Create your views here.
#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['contraseña']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'Login.html')

def new_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'newUser.html', {'form': form})

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

def registro_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después de guardar
    else:
        form = MascotaForm()
    return render(request, 'registro-mascota-perdida.html', {'form': form})



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
