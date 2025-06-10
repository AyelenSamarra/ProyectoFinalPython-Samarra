from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry
from Taberna.models import User 

admin.site.register(Tabernero)
admin.site.register(ClienteFrecuente)
admin.site.register(Producto)

LogEntry.user.field.remote_field.model = User