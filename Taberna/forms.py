from django import forms
from django.contrib.auth.forms  import UserCreationForm
from .models import User, Avatar
from django.contrib.auth.forms import UserChangeForm

class TaberneroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Tabernero', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Tabernero', required=True)
    edad = forms.IntegerField(label='Edad del Tabernero', required=True)


class ClienteFrecuenteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Cliente', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Cliente', required=True)
    pedido_favorito = forms.CharField(max_length=100, label='Pedido Favorito', required=True)


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Producto', required=True)
    precio = forms.CharField(max_length=100, label='Precio del Producto', required=True)
    stock = forms.IntegerField(label='Stock del Producto', required=True)


class BuscarProductoForm(forms.Form):
    query = forms.CharField(max_length=100, label='Buscar Producto por Nombre', required=False)
    def clean_query(self):
        query = self.cleaned_data.get('query')
        if not query:
            raise forms.ValidationError("Este campo es obligatorio.")
        return query
    

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "nombre", "apellido"]


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)   