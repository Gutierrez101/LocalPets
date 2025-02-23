from django import forms
from .models import tablaPrueva, tablaVinculada, Mascota

class tablaPruevaForm(forms.ModelForm):
    class Meta:
        model = tablaPrueva
        fields ='__all__'  # lista de campos de la base de datos a incluir
        
        
class tablaVinculadaForm(forms.ModelForm):
    class Meta:
        model = tablaVinculada
        fields = '__all__'  # lista de campos de la base de datos a incluir


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['especie', 'raza', 'color', 'tamaño', 'descripcion', 'estado', 'fotografia', 'latitud', 'longitud', 'direccion']