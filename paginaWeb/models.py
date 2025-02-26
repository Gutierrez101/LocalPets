from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class tablaPrueva(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    
    imajen = models.ImageField(upload_to="imagenes/", null=True)
    def __str__(self):
        return self.nombre
    
class tablaVinculada(models.Model):
    nombre = models.CharField(max_length=50)
    tablaPrueva = models.ForeignKey(tablaPrueva, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
#Modelo de mascotas  
class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    especie=models.CharField(max_length=50)
    raza=models.CharField(max_length=100,blank=True,null=True)
    color=models.CharField(max_length=50)
    tamaño=models.CharField(max_length=50,choices=[('Pequeño','Pequeño'),('Mediano','Mediano'),('Grande','Grande')])
    descripcion=models.TextField(blank=True,null=True)
    estado=models.CharField(max_length=50,choices=[('Perdido','Perdido'),('Adoptado','Adoptado'),('Disponible','Disponible')])
    fotografia=models.ImageField(upload_to='mascotas/',blank=True,null=True)
    latitud=models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    longitud=models.DecimalField(max_digits=9,decimal_places=6,blank=True,null=True)
    direccion=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f"{self.id}: {self.especie} - {self.raza if self.raza else 'Sin raza'} ({self.estado}) - {self.direccion if self.direccion else 'Sin dirección'}"

    
    def registrarMascota(self):
        self.save()
        return f"Mascota {self.especie}-{self.raza} registrada con exito."
    
    def eliminarMascota(self):
        self.delete()
        return f"Mascota {self.especie}-{self.raza} eleiminada con exito."
    
    def actualizarMascota(self,**kwargs):
        for key, value in kwargs.items():
            if hasattr(self,key):
                setattr(self,key,value)
        self.save()
        return f"Mascota {self.especie}-{self.raza if self.raza else 'Sin raza'} actualizada correctamente"
    
    def obtenerDetalles(self):
        return{
            "ID": self.id,
            "Especie": self.especie,
            "Raza":self.raza if self.raza else "Sin raza",
            "Color":self.color,
            "Tamaño":self.tamaño,
            "Descripcion":self.descripcion,
            "Estado":self.estado,
            "Fotografia": getattr(self.fotografia,'url',"No disponible"),
            "Direccion": self.direccion if self.direccion else "No especificada"
        }
    
    def obtenerUbicacion(self):
        return self.direccion if self.direccion else "Ubicacion no disponible"

    def actualizarUbicacion(self,nueva_direccion):
        self.direccion=nueva_direccion
        self.save()
        return f"Ubicacion actualizada a: {self.direccion}"



#Modelo de Publicacion
class Publicacion(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey('Usuario',on_delete=models.CASCADE)
    mascota=models.ForeignKey('Mascota',on_delete=models.CASCADE)
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    comentarios=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Publicacion de {self.usuario.username} sobre {self.mascota.especie}"
    
    def crearPublicacion(self,usuario,mascota,comentarios=""):
        self.usuario=usuario
        self.mascota=mascota
        self.comentarios=comentarios
        self.save()
        return f"Publicacion creada por {self.usuario.username} sobre {self.mascota.especie}"
    
    def editarPublicacion(self,nuevo_comentario):
        self.comentarios=nuevo_comentario
        self.save()
        return f"Publicacion editada correctamente"
    
    def eliminarPublicacion(self):
        self.delete()
        return f"Publicacion eliminada con exito"
    
    def agregarComentarios(self,nuevo_comentario):
        self.comentarios+=f"\n{nuevo_comentario}"
        self.save()
        return "Comentario agregado correctamente"
    
# Clase Usuario
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    # Nombre del usuario (máximo 50 caracteres)
    nombre = models.CharField(max_length=50)    
    email = models.EmailField(unique=True)
    # Contraseña del usuario (en una aplicación real debería encriptarse)
    contraseña = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        # Devuelve el nombre del usuario como objeto
        return self.nombre

    # Guarda el usuario en     
    def registrar(self):
        self.save()
        return f"Usuario {self.nombre} registrado con éxito."
    
    def iniciarSesion(self, email, password):
        # Verifica el email y la contraseña para iniciar sesión
        if self.email == email and self.contraseña == password:
            return f"Sesión iniciada para {self.nombre}."
        return "Credenciales inválidas."
    
    def cerrarSesion(self):
        # Simula el cierre de sesión del usuario
        return f"Sesión cerrada para {self.nombre}."
    
    def actualizarPerfil(self, **kwargs):
        # Actualiza los datos del usuario con los valores proporcionados
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
        return f"Perfil de {self.nombre} actualizado con éxito."
    
    def autenticacion(self, email, password):
        # Verifica si el email y la contraseña coinciden con los del usuario
        return self.email == email and self.contraseña == password