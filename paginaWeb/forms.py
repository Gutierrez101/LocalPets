from django import forms
from .models import tablaPrueva, tablaVinculada, Mascota, Usuario

# Formulario para la clase tablaPrueva
class tablaPruevaForm(forms.ModelForm):
    class Meta:
        model = tablaPrueva
        fields = '__all__'

# Formulario para la clase tablaVinculada
class tablaVinculadaForm(forms.ModelForm):
    class Meta:
        model = tablaVinculada
        fields = '__all__'

# Formulario para la clase Mascota
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['especie', 'raza', 'color', 'tamaño', 'descripcion', 'estado', 'fotografia', 'latitud', 'longitud', 'direccion']

# Formulario para la clase Usuario
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña', 'telefono']  # Los campos que queremos mostrar en el formulario

    # Valida que la contraseña tenga una longitud mínima
    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        if len(contraseña) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return contraseña
    
    # Valida si el email ya está registrado
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
