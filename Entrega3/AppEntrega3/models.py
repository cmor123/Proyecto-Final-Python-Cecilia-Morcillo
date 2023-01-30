from django.db import models

# Create your models here.

class Destino(models.Model):

    pais=models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)

    def __str__(self):
            return f"Nombre: {self.pais}, Ciudad {self.ciudad}"
   
class Hospedaje(models.Model):

    Tipo_Hospedaje= models.CharField(max_length=30)
    Zona= models.CharField(max_length=30)
    Cantidad_Personas= models.IntegerField()
    
    def __str__(self):
            return f"Hoteles: {self.Tipo_Hospedaje} - Zona: {self.Zona} - Casas: {self.Cantidad_Personas} "

class Alquiler_Coches(models.Model):
    Alta_Gama=models.CharField(max_length=30)
    Media_Gama= models.CharField(max_length=30)
    Compacto= models.CharField(max_length=30)
  
    def __str__(self):
            return f"Alta_Gama: {self.Alta_Gama} - Media_Gama {self.Media_Gama} - Compacto {self.Compacto} "
   

class Opiniones_Viajeros(models.Model):
     Nombre =  models.CharField(max_length=30)
     Nacionalidad = models.CharField(max_length=40)
     Opiniones = models.CharField(max_length=60)

     def __str__(self):
            return f"Nombre: {self.Nombre} - Nacionalidad: {self.Nacionalidad} - Opiniones: {self.Opiniones} "


from django.contrib.auth.models import User

class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}" 