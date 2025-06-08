from django.db import models
from django.contrib.auth.models import User

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
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"
    
    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatares'

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'