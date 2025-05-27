from django.urls import path
from . import views

app_name = 'Taberna'  # Add this for namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('taberneros/', views.taberneros, name='taberneros'),
    path('taberneros/<int:tabernero_id>/', views.detalle_taberneros, name='detalle_taberneros'),
    path('taberneros/form/', views.taberneros_form, name='taberneros_form'),
    path('clientes/', views.clientes_frecuentes, name='clientes_frecuentes'),
    path('clientes/<int:cliente_id>/', views.detalle_clientes_frecuentes, name='detalle_clientes'),
    path('clientes/form/', views.clientes_frecuentes_form, name='clientes_form'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('productos/form/', views.productos_form, name='productos_form'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
]