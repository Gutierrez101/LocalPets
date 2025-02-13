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
#Modelo de mascots  
class Mascota(models.Model):
    id=models.AutoField(primary_key=True)
    especie=models.CharField(max_length=50)
    raza=models.CharField(max_length=100,blank=True,null=True)
    color=models.CharField(max_length=50)
    tamaño=models.CharField(max_length=50,choices=[('Pequeño','Pequeño'),('Mediano','Mediano'),('Grande','Grande')])
    descripcion=models.TextField(blank=True,null=True)
    estado=models.CharField(max_length=50,choices=[('Perdido','Perdido'),('Adoptado','Adoptado'),('Disponible','Disponible')])
    fotografia=models.ImageField(upload_to='mascotas/',blank=True,null=True)
    direccion=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return f"{self.especie} - {self.raza if self.raza else 'sin raza'} ({self.estado})"
    
    def registrarMascota(self):
        self.save()
        return f"Mascota {self.especie}-{self.raza} registrada con exito."
    
    def eliminarMascota(self):
        self.delete()
        return f"Mascota {self.especie}-{self.raza} eleiminada con exito."
    
    def actualizarMascota(self,**kwargs):
        for key, value in kwargs.item():
            if hasattr(self,key):
                setattr(self,key,value)
        self.save()
        return f"Mascota {self.especie}-{self.raza} actualizada correctamente"
    
    def obtenerDetalles(self):
        return{
            "ID": self.id,
            "Especie": self.especie,
            "Raza":self.raza if self.raza else "Sin raza",
            "Color":self.color,
            "Tamaño":self.tamaño,
            "Descripcion":self.descripcion,
            "Estado":self.estado,
            "Fotografia": self.fotografia.url if self.fotografia else "No disponible",
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
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
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