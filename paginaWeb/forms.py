from django import forms
from .models import tablaPrueva, tablaVinculada

class tablaPruevaForm(forms.ModelForm):
    class Meta:
        model = tablaPrueva
        fields ='__all__'  # lista de campos de la bace de datos a incluir
        
        
class tablaVinculadaForm(forms.ModelForm):
    class Meta:
        model = tablaVinculada
        fields = '__all__'  # lista de campos de la bace de datos a incluir
