from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = 'Taberna'  # Add this for namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('comentarios/', views.comentarios, name='comentarios'),
    path('crear_comentario/', views.crear_comentario, name='crear_comentario'),

    #Taberneros

    path('taberneros/', views.TaberneroListView.as_view(), name='taberneros'),
    path('taberneros/detail/<int:pk>/', views.TaberneroDetailView.as_view(), name='detalle_taberneros'),
    path('taberneros/create/', views.TaberneroCreateView.as_view(), name='crear_tabernero'),
    path('taberneros/update/<int:pk>/', views.TaberneroUpdateView.as_view(), name='actualizar_tabernero'),
    path('taberneros/delete/<int:pk>/', views.TaberneroDeleteView.as_view(), name='tabernero_confirm_delete'),


    #Clientes Frecuentes

    path('clientes/', views.ClienteFrecuenteListView.as_view(), name='clientes_frecuentes'),
    path('clientes/detail/<int:pk>/', views.ClienteFrecuenteDetailView.as_view(), name='detalle_clientes_frecuentes'),
    path('clientes/create/', views.ClienteFrecuenteCreateView.as_view(), name='crear_cliente_frecuente'),
    path('clientes/update/<int:pk>/', views.ClienteFrecuenteUpdateView.as_view(), name='actualizar_cliente_frecuente'),
    path('clientes/delete/<int:pk>/', views.ClienteFrecuenteDeleteView.as_view(), name='cliente_frecuente_confirm_delete'),


    # Productos
    
    path('productos/', views.ProductoListView.as_view(), name='productos'),
    path('productos/detail/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle_productos'),
    path('productos/create/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/update/<int:pk>/', views.ProductoUpdateView.as_view(), name='actualizar_producto'),
    path('productos/delete/<int:pk>/', views.ProductoDeleteView.as_view(), name='producto_confirm_delete'),
    path('productos/buscar/', views.BuscarProductoView.as_view(), name='buscar_producto'),

    # Perfil y Autenticación
    path('registro/', views.register, name="registro"),
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='Taberna/logout.html'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar_avatar/', views.agregar_avatar, name="agregar_avatar"),
    path('password_cambio/', views.password_cambio, name='password_cambio'),
    path('password_exito/', views.password_exito, name='password_exito'),
]
    