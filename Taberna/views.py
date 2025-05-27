from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    return render(request, 'Taberna/index.html')

def taberneros(request):
    taberneros = Tabernero.objects.all()
    return render(request, 'Taberna/taberneros.html', {'taberneros': taberneros})

def detalle_taberneros(request, tabernero_id):
    tabernero = get_object_or_404(Tabernero, id=tabernero_id)
    return render(request, 'Taberna/detalle_taberneros.html', {'tabernero': tabernero})

def taberneros_form(request):
    if request.method == 'POST':
        form = TaberneroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            edad = form.cleaned_data['edad']
            tabernero = Tabernero(nombre=nombre, apellido=apellido, edad=edad)
            tabernero.save()
            taberneros = Tabernero.objects.all()
            return render(request, 'Taberna/taberneros.html', {'taberneros': taberneros})
    else:
        form = TaberneroForm()
    return render(request, 'Taberna/taberneros_form.html', {'form': form})

def clientes_frecuentes(request, cliente_id=None):
    clientes_frecuentes = ClienteFrecuente.objects.all()
    return render(request, 'Taberna/clientes_frecuentes.html', {'clientes_frecuentes': clientes_frecuentes})

def detalle_clientes_frecuentes(request, cliente_id):
    cliente = get_object_or_404(ClienteFrecuente, id=cliente_id)
    return render(request, 'Taberna/detalle_clientes_frecuentes.html', {'cliente': cliente})

def clientes_frecuentes_form(request):
    if request.method == 'POST':
        form = ClienteFrecuenteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            pedido_favorito = form.cleaned_data['pedido_favorito']
            cliente = ClienteFrecuente(nombre=nombre, apellido=apellido, pedido_favorito=pedido_favorito)
            cliente.save()
            clientes_frecuentes = ClienteFrecuente.objects.all()
            return render(request, 'Taberna/clientes_frecuentes.html', {'clientes_frecuentes': clientes_frecuentes})
    else:
        form = ClienteFrecuenteForm()
    return render(request, 'Taberna/clientes_frecuentes_form.html', {'form': form})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'Taberna/productos.html', {'productos': productos})

def detalle_productos(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'Taberna/detalle_productos.html', {'producto': producto})

def productos_form(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            producto = Producto(nombre=nombre, precio=precio, stock=stock)
            producto.save()
            productos = Producto.objects.all()
            return render(request, 'Taberna/productos.html', {'productos': productos})
    else:
        form = ProductoForm()
    return render(request, 'Taberna/productos_form.html', {'form': form})

def buscar_productos(request):
    productos = None  # Inicializar productos como None por defecto
    if request.method == 'POST':
        form = BuscarProductoForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            productos = Producto.objects.filter(nombre__icontains=query)
    else:
        form = BuscarProductoForm()

    return render(request, 'Taberna/buscar_producto.html', {
        'form': form,
        'productos': productos  # Esto puede ser None o una lista de resultados
    })



