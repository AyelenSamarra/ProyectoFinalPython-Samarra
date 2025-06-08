from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import AvatarForm

def index(request):
    return render(request, 'Taberna/index.html')

# -------------------------------------------------Taberneros-------------------------------------------------

# Crear: 

def crear_tabernero(request):
    if request.method == 'POST':
        form = TaberneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Taberna:taberneros')
    else:
        form = TaberneroForm()
    return render(request, 'Taberna/crear_tabernero.html', {'form': form})

class TaberneroCreateView(CreateView):
    model = Tabernero
    form_class = TaberneroForm
    template_name = 'Taberna/crear_tabernero.html'
    success_url = reverse_lazy('Taberna:taberneros')

class TaberneroListView(ListView):
    model = Tabernero
    template_name = 'Taberna/taberneros.html'
    context_object_name = 'taberneros'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

# Leer:

def listar_taberneros(request):
    taberneros = Tabernero.objects.all()
    return render(request, 'Taberna/taberneros.html', {'taberneros': taberneros})

class TaberneroDetailView(DetailView):
    model = Tabernero
    template_name = 'Taberna/detalle_taberneros.html'
    context_object_name = 'tabernero'

# Actualizar:

def actualizar_tabernero(request, pk):
    tabernero = get_object_or_404(Tabernero, pk=pk)
    if request.method == 'POST':
        form = TaberneroForm(request.POST, instance=tabernero)
        if form.is_valid():
            form.save()
            return redirect('Taberna:taberneros')
    else:
        form = TaberneroForm(instance=tabernero)
    return render(request, 'Taberna/actualizar_tabernero.html', {'form': form, 'tabernero': tabernero})

class TaberneroUpdateView(UpdateView):
    model = Tabernero
    form_class = TaberneroForm
    template_name = 'Taberna/actualizar_tabernero.html'
    success_url = reverse_lazy('Taberna:taberneros')

# Eliminar:

def eliminar_tabernero(request, pk):
    tabernero = get_object_or_404(Tabernero, pk=pk)
    tabernero.delete()
    return redirect('Taberna:taberneros')


class TaberneroDeleteView(DeleteView):
    model = Tabernero
    success_url = reverse_lazy('Taberna:taberneros')



# -------------------------------------------------Clientes Frecuentes-------------------------------------------------

# Crear: 

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteFrecuenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Taberna:clientes_frecuentes')
    else:
        form = ClienteFrecuenteForm()
    return render(request, 'Taberna/clientes_frecuentes.html', {'form': form})

class ClienteFrecuenteCreateView(CreateView):
    model = ClienteFrecuente
    form_class = ClienteFrecuenteForm
    template_name = 'Taberna/crear_cliente.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')

class ClienteFrecuenteListView(ListView):
    model = ClienteFrecuente
    template_name = 'Taberna/clientes_frecuentes.html'
    context_object_name = 'clientes_frecuentes'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

# Leer:

def listar_clientes(request):
    clientes_frecuentes = ClienteFrecuente.objects.all()
    return render(request, 'Taberna/clientes_frecuentes.html', {'clientes_frecuentes': clientes_frecuentes})

class ClienteFrecuenteDetailView(DetailView):
    model = ClienteFrecuente
    template_name = 'Taberna/detalle_clientes_frecuentes.html'
    context_object_name = 'cliente_frecuente'


# Actualizar:

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(ClienteFrecuente, pk=pk)
    if request.method == 'POST':
        form = ClienteFrecuenteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('Taberna:clientes_frecuentes')
    else:
        form = ClienteFrecuenteForm(instance=cliente)
    return render(request, 'Taberna/actualizar_cliente_frecuente.html', {'form': form, 'cliente': cliente})

class ClienteFrecuenteUpdateView(UpdateView):
    model = ClienteFrecuente
    form_class = ClienteFrecuenteForm
    template_name = 'Taberna/actualizar_cliente_frecuente.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')

# Eliminar:

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(ClienteFrecuente, pk=pk)
    cliente.delete()
    return redirect('Taberna:clientes_frecuentes')

class ClienteFrecuenteDeleteView(DeleteView):
    model = ClienteFrecuente
    template_name = 'Taberna/cliente_frecuente_confirm_delete.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')



# -------------------------------------------------Productos-------------------------------------------------

# Crear:
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Taberna:productos')
    else:
        form = ProductoForm()
    return render(request, 'Taberna/crear_producto.html', {'form': form})

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Taberna/crear_producto.html'
    success_url = reverse_lazy('Taberna:productos')

class ProductoListView(ListView):
    model = Producto
    template_name = 'Taberna/productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset

# Leer:
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'Taberna/productos.html', {'productos': productos})

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'Taberna/detalle_productos.html'
    context_object_name = 'producto'


# Actualizar:
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('Taberna:productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Taberna/actualizar_producto.html', {'form': form, 'producto': producto})

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Taberna/actualizar_producto.html'
    success_url = reverse_lazy('Taberna:productos')


# Eliminar:
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('Taberna:productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('Taberna:productos')

# Buscar:

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
        'productos': productos
        })

class BuscarProductoView(ListView):
    model = Producto
    template_name = 'Taberna/buscar_producto.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', None)
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset


# -------------------------------------------------Login-------------------------------------------------

@login_required

def editar_perfil(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Taberna:index')
    else:
        form = UserCreationForm(instance=request.user)
    return render(request, 'Taberna/editar_perfil.html', {'form': form})

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=request.user.avatar)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AvatarForm(instance=request.user.avatar)
    return render(request, 'Taberna/upload_avatar.html', {'form': form})