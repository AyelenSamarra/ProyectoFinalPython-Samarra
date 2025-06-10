from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'Taberna/home.html')

# -------------------------------------------------Taberneros-------------------------------------------------

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

class TaberneroDetailView(DetailView):
    model = Tabernero
    template_name = 'Taberna/detalle_taberneros.html'
    context_object_name = 'tabernero'

class TaberneroUpdateView(UpdateView):
    model = Tabernero
    form_class = TaberneroForm
    template_name = 'Taberna/actualizar_tabernero.html'
    success_url = reverse_lazy('Taberna:taberneros')

class TaberneroDeleteView(DeleteView):
    model = Tabernero
    success_url = reverse_lazy('Taberna:taberneros')


# -------------------------------------------------Clientes Frecuentes-------------------------------------------------

# Crear: 

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

class ClienteFrecuenteDetailView(DetailView):
    model = ClienteFrecuente
    template_name = 'Taberna/detalle_clientes_frecuentes.html'
    context_object_name = 'cliente_frecuente'

class ClienteFrecuenteUpdateView(UpdateView):
    model = ClienteFrecuente
    form_class = ClienteFrecuenteForm
    template_name = 'Taberna/actualizar_cliente_frecuente.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')

class ClienteFrecuenteDeleteView(DeleteView):
    model = ClienteFrecuente
    template_name = 'Taberna/cliente_frecuente_confirm_delete.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')


# -------------------------------------------------Productos-------------------------------------------------

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

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'Taberna/detalle_productos.html'
    context_object_name = 'producto'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Taberna/actualizar_producto.html'
    success_url = reverse_lazy('Taberna:productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('Taberna:productos')


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


# ------------------------------------------------- Registracion / Login / Logout-------------------------------------------------

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy("Taberna:home"))
    else:
        miForm = RegistroForm()

    return render(request, "Taberna/registro.html", {"form": miForm})

def loginRequest(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            username = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)            
            return redirect("Taberna:home")
        else:
            return redirect(reverse_lazy("Taberna:login"))
    
    else:
        miForm = AuthenticationForm()

    return render(request, "Taberna/login.html", {"form": miForm})