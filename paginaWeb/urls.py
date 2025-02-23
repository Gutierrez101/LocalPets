from django.urls import path

from .views import (
    index, ingresarTabla1, ingresarTabla2, verTabla1s, verTabla1Unica,
    obtener_detalles, actualizar_mascota, obtener_ubicacion, actualizar_ubicacion, login_view, new_user_view
)
#from .views import obtener_detalles,actualizar_mascota,obtener_ubicacion,actualizar_ubicacion
urlpatterns = [
    path("", index, name="index"),
    path("ingresarTabla1/", ingresarTabla1, name="ingresarTabla1"),
    path("ingresarTabla2/", ingresarTabla2, name="ingresarTabla2"),
    path("verTabla1s/", verTabla1s, name="verTabla1s"),
    path("verTabla1Unica/<int:id>/", verTabla1Unica, name="verTabla1Unica"),
    path('login/', login_view, name='login'),
    path('new_user/', new_user_view, name='new_user'),
    path('mascota/<int:pk>/',obtener_detalles,name='obtener_detalles'),
    path('mascota/<int:pk>/actualizar/', actualizar_mascota, name='actualizar_mascota'),
    path('mascota/<int:pk>/ubicacion/', obtener_ubicacion, name='obtener_ubicacion'),
    path('mascota/<int:pk>/ubicacion/actualizar/', actualizar_ubicacion, name='actualizar_ubicacion'),
    
]