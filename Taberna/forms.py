from django import forms
from .models import Tabernero, ClienteFrecuente, Producto

class TaberneroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Tabernero', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Tabernero', required=True)
    edad = forms.IntegerField(label='Edad del Tabernero', required=True)
    class Meta:
        model = Tabernero
        fields = ['nombre', 'apellido', 'edad']

class ClienteFrecuenteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Cliente', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Cliente', required=True)
    pedido_favorito = forms.CharField(max_length=100, label='Pedido Favorito', required=True)
    class Meta:
        model = ClienteFrecuente
        fields = ['nombre', 'apellido', 'pedido_favorito']

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Producto', required=True)
    precio = forms.CharField(max_length=100, label='Precio del Producto', required=True)
    stock = forms.IntegerField(label='Stock del Producto', required=True)
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']

class BuscarProductoForm(forms.Form):
    query = forms.CharField(max_length=100, label='Buscar Producto por Nombre', required=False)
    def clean_query(self):
        query = self.cleaned_data.get('query')
        if not query:
            raise forms.ValidationError("Este campo es obligatorio.")
        return query