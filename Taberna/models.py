from django.db import models

class Tabernero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ClienteFrecuente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pedido_favorito = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"