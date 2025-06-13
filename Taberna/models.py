from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils import timezone

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
    nombre = models.CharField(
        max_length=100, 
        verbose_name="Nombre del producto",
    )
    precio = models.CharField( 
        max_length=100, 
        verbose_name="Precio",
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="Unidades disponibles"
    )
    categoria = models.CharField(
    max_length=50,
    verbose_name="Categoría",
    choices=[
        ('comida', 'Comida'),
        ('bebida', 'Bebida'),
        ('postre', 'Postre')
    ],
    default='comida'  # Add this line
    )

     # Texto enriquecido (Requisito - CKEditor)
    descripcion = RichTextField(
        verbose_name="Descripción detallada",
        blank=True,
        help_text="Ingredientes, preparación, maridaje..."
    )
    # Campo de imagen
    imagen = models.ImageField(
        upload_to='productos/',
        verbose_name="Foto del producto",
        null=True,
        blank=True
    )
    # Campo de fecha
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación en el menú"
    )
    es_destacado = models.BooleanField(
        default=False,
        verbose_name="¿Producto destacado?"
    )

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

    class Meta:
        verbose_name = "Producto del menú"
        verbose_name_plural = "Productos del menú"
        ordering = ['-fecha_creacion']
    



class User(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
 