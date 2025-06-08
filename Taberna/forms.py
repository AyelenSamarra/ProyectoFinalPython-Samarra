from django import forms
from .models import Tabernero, ClienteFrecuente, Producto

class TaberneroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Tabernero', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Tabernero', required=True)
    edad = forms.IntegerField(label='Edad del Tabernero', required=True)
    
    def save(self, commit=True):
        tabernero = Tabernero(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            edad=self.cleaned_data['edad']
        )
        if commit:
            tabernero.save()
        return tabernero


class ClienteFrecuenteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Cliente', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Cliente', required=True)
    pedido_favorito = forms.CharField(max_length=100, label='Pedido Favorito', required=True)

    def save(self, commit=True):
        cliente = ClienteFrecuente(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            pedido_favorito=self.cleaned_data['pedido_favorito']
        )
        if commit:
            cliente.save()
        return cliente


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Producto', required=True)
    precio = forms.CharField(max_length=100, label='Precio del Producto', required=True)
    stock = forms.IntegerField(label='Stock del Producto', required=True)

    def save(self, commit=True):
        producto = Producto(
            nombre=self.cleaned_data['nombre'],
            precio=self.cleaned_data['precio'],
            stock=self.cleaned_data['stock']
        )
        if commit:
            producto.save()
        return producto

class BuscarProductoForm(forms.Form):
    query = forms.CharField(max_length=100, label='Buscar Producto por Nombre', required=False)
    def clean_query(self):
        query = self.cleaned_data.get('query')
        if not query:
            raise forms.ValidationError("Este campo es obligatorio.")
        return query