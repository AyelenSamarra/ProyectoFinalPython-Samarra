from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.conf import settings
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'Taberna/home.html', context)

def about(request):
    return render(request, 'Taberna/about.html')


@login_required
def comentarios(request):
    comentarios_list = Comentario.objects.all().order_by('-fecha_creacion')
    return render(request, 'Taberna/comentarios.html', {'comentarios': comentarios_list})

@login_required
def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            # Save the comment with the logged-in user's information
            comentario = Comentario(
                nombre=f"{request.user.nombre} {request.user.apellido}",
                email=request.user.email,
                mensaje=form.cleaned_data['mensaje']
            )
            comentario.save()
            messages.success(request, 'Comentario enviado correctamente.')
            return redirect('Taberna:comentarios')
    else:
        form = ComentarioForm()

    return render(request, 'Taberna/crear_comentario.html', {'form': form})

# -------------------------------------------------Taberneros-------------------------------------------------

class TaberneroListView(ListView):
    model = Tabernero
    template_name = 'Taberna/taberneros.html'
    context_object_name = 'taberneros'

class TaberneroCreateView(LoginRequiredMixin, CreateView):
    model = Tabernero
    fields = ["nombre", "apellido", "edad", "descripcion"]
    template_name = 'Taberna/crear_tabernero.html'
    success_url = reverse_lazy('Taberna:taberneros')

class TaberneroDetailView(DetailView):
    model = Tabernero
    template_name = 'Taberna/detalle_taberneros.html'
    context_object_name = 'tabernero'

class TaberneroUpdateView(LoginRequiredMixin, UpdateView):
    model = Tabernero
    fields = ["nombre", "apellido", "edad", "descripcion"]
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
    fields = ["nombre", "apellido", "pedido_favorito", "estado"]
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
    fields = ["nombre", "apellido", "pedido_favorito", "estado"]
    template_name = 'Taberna/actualizar_cliente_frecuente.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')

class ClienteFrecuenteDeleteView(LoginRequiredMixin, DeleteView):
    model = ClienteFrecuente
    template_name = 'Taberna/cliente_frecuente_confirm_delete.html'
    success_url = reverse_lazy('Taberna:clientes_frecuentes')


# -------------------------------------------------Productos-------------------------------------------------

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm  # <- ahora usa tu formulario
    template_name = 'Taberna/crear_producto.html'
    success_url = reverse_lazy('Taberna:productos')

class ProductoListView(ListView):
    model = Producto
    template_name = 'Taberna/productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get search term and category from URL parameters
        busqueda = self.request.GET.get('busqueda')
        categoria = self.request.GET.get('categoria')
        
        # Apply search filter if term exists
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        
        # Apply category filter if specified and not 'todos'
        if categoria and categoria != 'todos':
            queryset = queryset.filter(categoria=categoria)
        
        return queryset.order_by('nombre')  # Or your preferred ordering

class ProductoDetailView(DetailView):
    model = Producto
    fields = ["nombre", "precio", "stock", "descripcion", "imagen", "categoria"]
    template_name = 'Taberna/detalle_productos.html'
    context_object_name = 'producto'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
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
        try:
            form = RegistroForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('Taberna:home')
            else:
                print("Form errors:", form.errors)  # Debug output
        except Exception as e:
            print("Registration error:", str(e))  # Debug output
            raise  # Re-raise the error after logging it
    else:
        form = RegistroForm()
    
    return render(request, "Taberna/registro.html", {"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Handle avatar
                try:
                    avatar = Avatar.objects.get(user=user).imagen.url
                except Avatar.DoesNotExist:
                    avatar = "/media/avatares/default.jpeg"
                request.session['avatar'] = avatar  # Store in session if needed
                return redirect('Taberna:home')  # Use redirect instead of render
        return render(request, "Taberna/login.html", {"form": form, "error": "Invalid credentials"})
    
    form = AuthenticationForm()
    return render(request, "Taberna/login.html", {"form": form})


# ------------------------------------------------- Editar Perfil -------------------------------------------------
@login_required
def perfil(request):
    usuario = request.user
    try:
        avatar = Avatar.objects.get(user=usuario.id).imagen.url
    except Avatar.DoesNotExist:
        avatar = "/media/avatares/default.jpeg"
    
    return render(request, "Taberna/perfil.html", {"usuario": usuario, "avatar": avatar})


@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            # Handle profile-specific fields
            profile, created = Profile.objects.get_or_create(user=user)
            profile.biografia = form.cleaned_data.get('biografia')
            profile.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            profile.save()
            
            user.save()  # This saves the User model fields
            return redirect('Taberna:perfil')  # Redirect to profile page
    else:
        initial_data = {
            'biografia': request.user.profile.biografia,
            'fecha_nacimiento': request.user.profile.fecha_nacimiento
        }
        form = UserEditForm(instance=request.user, initial=initial_data)
    
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

@login_required
def password_exito(request):
    return render(request, "Taberna/password_exito.html")

@login_required
def password_cambio(request):
    if request.method == "POST":
        form = PasswordCambioForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Importante para no cerrar sesión
            return redirect('Taberna:password_exito')
    else:
        form = PasswordCambioForm(user=request.user)
    return render(request, 'Taberna/password_cambio.html', {'form': form})