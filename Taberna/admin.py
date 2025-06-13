from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry
from Taberna.models import User 

admin.site.register(Tabernero)
admin.site.register(ClienteFrecuente)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'es_destacado')
    list_filter = ('categoria', 'es_destacado')
    search_fields = ('nombre', 'descripcion')
    date_hierarchy = 'fecha_creacion'

LogEntry.user.field.remote_field.model = User