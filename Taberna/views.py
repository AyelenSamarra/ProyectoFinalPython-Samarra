from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



def home(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'Taberna/home.html', context)


def about(request):
    return render(request, 'Taberna/about.html')

# -------------------------------------------------Taberneros-------------------------------------------------

class TaberneroListView(ListView):
    model = Tabernero
    template_name = 'Taberna/taberneros.html'
    context_object_name = 'taberneros'

class TaberneroCreateView(LoginRequiredMixin, CreateView):
    model = Tabernero
    fields = ["nombre", "apellido", "edad"]
    template_name = 'Taberna/crear_tabernero.html'
    success_url = reverse_lazy('Taberna:taberneros')

class TaberneroDetailView(DetailView):
    model = Tabernero
    template_name = 'Taberna/detalle_taberneros.html'
    context_object_name = 'tabernero'

class TaberneroUpdateView(LoginRequiredMixin, UpdateView):
    model = Tabernero
    fields = ["nombre", "apellido", "edad"]
    template_name = 'Taberna/actualizar_tabernero.html'
    success_url = reverse_lazy('Taberna:taberneros')

class TaberneroDeleteView(LoginRequiredMixin, DeleteView):
    model = Tabernero
    template_name = 'Taberna/tabernero_confirm_delete.html'
    success_url = reverse_lazy('Taberna:taberneros')


# -------------------------------------------------Clientes Frecuentes-------------------------------------------------

# Crear: 

class ClienteFrecuenteCreateView(LoginRequiredMixin, CreateView):
    model = ClienteFrecuente
    fields = ["nombre", "apellido", "pedido_favorito"]
    template_name = 'Taberna/crear_cliente_frecuente.html'
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

class ClienteFrecuenteUpdateView(LoginRequiredMixin, UpdateView):
    model = ClienteFrecuente
    fields = ["nombre", "apellido", "pedido_favorito"]
    template_name = 'Taberna/actualizar_cliente_frecuente.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')

class ClienteFrecuenteDeleteView(LoginRequiredMixin, DeleteView):
    model = ClienteFrecuente
    template_name = 'Taberna/cliente_frecuente_confirm_delete.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')


# -------------------------------------------------Productos-------------------------------------------------

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ["nombre", "precio", "stock"]
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

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ["nombre", "precio", "stock"]
    template_name = 'Taberna/actualizar_producto.html'
    success_url = reverse_lazy('Taberna:productos')

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'Taberna/producto_confirm_delete.html'
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
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('Taberna:home'))
    else:
        form = RegistroForm()

    return render(request, "Taberna/registro.html", {"form": form})   

def login_request(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.jpg"
            finally:
                request.session["avatar"] = avatar
            #__            
            return render(request, "Taberna/home.html")
        else:
            return redirect(reverse_lazy('Taberna:login'))
    else:
        form = AuthenticationForm()

    return render(request, "Taberna/login.html", {"form": form})


# ------------------------------------------------- Editar Perfil -------------------------------------------------

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=usuario)
            user.email = form.cleaned_data.get("email")
            user.nombre = form.cleaned_data.get("nombre")
            user.apellido = form.cleaned_data.get("apellido")
            user.save()
            return redirect(reverse_lazy("Taberna:home"))
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "Taberna/editar_perfil.html", {"form": form})

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = form.cleaned_data["imagen"]
            #Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #_________________________________
            return redirect(reverse_lazy("Taberna:home"))
    else:
        form = AvatarForm()
    return render(request, "Taberna/agregar_avatar.html", {"form": form})  