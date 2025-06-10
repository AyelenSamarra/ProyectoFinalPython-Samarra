from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

app_name = 'Taberna'  # Add this for namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('/<nombre>/<apellido>/', views.home, name='home'),

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

    # Login
    path('registro/', views.register, name="registro"),
    path('login/', views.loginRequest, name="login"),
    path('logout/', LogoutView.as_view(next_page='Taberna:home'), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    