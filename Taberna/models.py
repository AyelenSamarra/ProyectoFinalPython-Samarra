from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Tabernero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField(
        verbose_name="Descripción del tabernero",
        default="Tabernero experimentado en la cocina y el servicio al cliente.",
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ClienteFrecuente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pedido_favorito = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=1,
        choices=[
            ('A', 'Avistado'),
            ('D', 'Desaparecido'),
        ],
        default='A',  # Default to 'Avistado'
        verbose_name="Estado del cliente"
    )
    descripcion = models.TextField(
        verbose_name="Descripción del cliente",
        default="Cliente frecuente que disfruta de nuestros platos y bebidas.",
    )                                             

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
    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class User(AbstractUser):
    # Add your custom fields
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'Taberna_user'
    
    REQUIRED_FIELDS = ['email']
    
    def get_short_name(self):
        return self.nombre or self.username 
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
    
class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Contacto de {self.nombre} - {self.email}"
    
    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ['-fecha_creacion']