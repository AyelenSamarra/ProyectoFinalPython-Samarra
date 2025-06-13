from datetime import timezone, datetime
from django import forms
from django.contrib.auth.forms  import UserCreationForm, PasswordChangeForm
from .models import User, Avatar
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy

class TaberneroForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Tabernero', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Tabernero', required=True)
    edad = forms.IntegerField(label='Edad del Tabernero', required=True)
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label='Descripción del Tabernero',
        required=True,
        max_length=500
    )


class ClienteFrecuenteForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, label='Nombre del Cliente', required=True)
    apellido = forms.CharField(max_length=100, label='Apellido del Cliente', required=True)
    pedido_favorito = forms.CharField(max_length=100, label='Pedido Favorito', required=True)
    estado = forms.ChoiceField(
        choices=[
            ('A', 'Avistado'),
            ('D', 'Desaparecido'),
        ],
        label='Estado del Cliente',
        required=True,
        initial='A'  # Default to 'Avistado'
    )
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label='Descripción del Cliente',
        required=True,
        max_length=500
    )


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
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize field labels if needed
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar Contraseña"
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create profile for the new user
            from .models import Profile
            Profile.objects.create(user=user)
        return user


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(required=True)
    biografia = forms.CharField(widget=forms.Textarea, required=False)
    fecha_nacimiento = forms.DateField(label="Fecha de Nacimiento", required=False, widget=forms.SelectDateWidget(years=range(1900, datetime.now().year+1)))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'biografia', 'fecha_nacimiento']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)   


class PasswordCambioForm(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput, required=True)
    new_password1 = forms.CharField(label="Nueva Contraseña", widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(label="Confirmar Nueva Contraseña", widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_url = reverse_lazy('Taberna:password_exito')

class ComentarioForm(forms.Form):
    mensaje = forms.CharField(
        widget=forms.Textarea,
        label='Tu Comentario',
        required=True,
        max_length=1000
    )