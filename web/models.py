from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(null=True)
    contacto = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=13)
    telefono2 = models.CharField(max_length=13)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='productos',blank=True)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre
