from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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



# Nuevos Forms para creación, edición, etc.

# -------------------------------------------------Taberneros-------------------------------------------------
# Crear: 

# def crear_tabernero(request):
#     if request.method == 'POST':
#         form = TaberneroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Taberna:taberneros')
#     else:
#         form = TaberneroForm()
#     return render(request, 'Taberna/crear_tabernero.html', {'form': form})

# Leer:

# def listar_taberneros(request):
#     taberneros = Tabernero.objects.all()
#     return render(request, 'Taberna/taberneros.html', {'taberneros': taberneros})

# Actualizar:

# def actualizar_tabernero(request, pk):
#     tabernero = get_object_or_404(Tabernero, pk=pk)
#     if request.method == 'POST':
#         form = TaberneroForm(request.POST, instance=tabernero)
#         if form.is_valid():
#             form.save()
#             return redirect('Taberna:taberneros')
#     else:
#         form = TaberneroForm(instance=tabernero)
#     return render(request, 'Taberna/actualizar_tabernero.html', {'form': form, 'tabernero': tabernero})

# Eliminar:

# def eliminar_tabernero(request, pk):
#     tabernero = get_object_or_404(Tabernero, pk=pk)
#     tabernero.delete()
#     return redirect('Taberna:taberneros')

# class TaberneroListView(ListView):
#     model = Tabernero
#     template_name = 'Taberna/listar_taberneros.html'
#     context_object_name = 'taberneros'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         busqueda = self.request.GET.get('busqueda', None)
#         if busqueda:
#             queryset = queryset.filter(nombre__icontains=busqueda)
#         return queryset

# class TaberneroDetailView(DetailView):
#     model = Tabernero
#     template_name = 'Taberna/detalle_tabernero.html'
#     context_object_name = 'tabernero'

# class TaberneroDeleteView(DeleteView):
#     model = Tabernero
#     success_url = reverse_lazy('Taberna:taberneros')

# -------------------------------------------------Clientes Frecuentes-------------------------------------------------
# Crear: 

# def crear_cliente(request):
#     if request.method == 'POST':
#         form = ClienteFrecuenteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Taberna:clientes_frecuentes')
#     else:
#         form = ClienteFrecuenteForm()
#     return render(request, 'Taberna/clientes_frecuentes.html', {'form': form})

# Leer:

# def listar_clientes(request):
#     clientes_frecuentes = ClienteFrecuente.objects.all()
#     return render(request, 'Taberna/listar_clientes.html', {'clientes_frecuentes': clientes_frecuentes})

# Actualizar:

# def actualizar_cliente(request, pk):
#     cliente = get_object_or_404(Cliente, pk=pk)
#     if request.method == 'POST':
#         form = ClienteFrecuenteForm(request.POST, instance=cliente)
#         if form.is_valid():
#             form.save()
#             return redirect('Taberna:clientes_frecuentes')
#     else:
#         form = ClienteFrecuenteForm(instance=cliente)
#     return render(request, 'Taberna/actualizar_cliente.html', {'form': form, 'cliente': cliente})

# Eliminar:

# def eliminar_cliente(request, pk):
#     cliente = get_object_or_404(ClienteFrecuente, pk=pk)
#     cliente.delete()
#     return redirect('Taberna:clientes_frecuentes')

# class ClienteListView(ListView):
#     model = ClienteFrecuente
#     template_name = 'Taberna/clientes_frecuentes.html'
#     context_object_name = 'clientes_frecuentes'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         busqueda = self.request.GET.get('busqueda', None)
#         if busqueda:
#             queryset = queryset.filter(nombre__icontains=busqueda)
#         return queryset

# class ClienteFrecuenteDetailView(DetailView):
#     model = ClienteFrecuente
#     template_name = 'Taberna/detalle_cliente.html'
#     context_object_name = 'cliente_frecuente'

# -------------------------------------------------Productos-------------------------------------------------
# Crear:
# def crear_producto(request):
#     if request.method == 'POST':
#         form = ProductoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('Taberna:productos')
#     else:
#         form = ProductoForm()
#     return render(request, 'Taberna/crear_producto.html', {'form': form})
#
# Leer:
# def listar_productos(request):
#     productos = Producto.objects.all()
#     return render(request, 'Taberna/productos.html', {'productos': productos})
# Actualizar:
# def actualizar_producto(request, pk):
#     producto = get_object_or_404(Producto, pk=pk)
#     if request.method == 'POST':
#         form = ProductoForm(request.POST, instance=producto)
#         if form.is_valid():
#             form.save()
#             return redirect('Taberna:productos')
#     else:
#         form = ProductoForm(instance=producto)
#     return render(request, 'Taberna/actualizar_producto.html', {'form': form, 'producto': producto})
# Eliminar:
# def eliminar_producto(request, pk):
#     producto = get_object_or_404(Producto, pk=pk)
#     producto.delete()
#     return redirect('Taberna:productos')
# class ProductoListView(ListView):
#     model = Producto
#     template_name = 'Taberna/productos.html'
#     context_object_name = 'productos'
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         busqueda = self.request.GET.get('busqueda', None)
#         if busqueda:
#             queryset = queryset.filter(nombre__icontains=busqueda)
#         return queryset
# class ProductoDetailView(DetailView):
#     model = Producto
#     template_name = 'Taberna/detalle_producto.html'
#     context_object_name = 'producto'