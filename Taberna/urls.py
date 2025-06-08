from django.urls import path
from . import views

app_name = 'Taberna'  # Add this for namespace

urlpatterns = [
    path('', views.index, name='index'),

    #Taberneros
    path('taberneros/', views.taberneros, name='taberneros'),
    path('taberneros/<int:tabernero_id>/', views.detalle_taberneros, name='detalle_taberneros'),
    path('taberneros/form/', views.taberneros_form, name='taberneros_form'),
    #path('taberneros/list/', views.TaberneroListView.as_view(), name='taberneros_list'),
    #path('taberneros/detail/<int:pk>/', views.TaberneroDetailView.as_view(), name='detalle_tabernero'),
    #path('taberneros/create/', views.TaberneroCreateView.as_view(), name='crear_tabernero'),
    #path('taberneros/update/<int:pk>/', views.TaberneroUpdateView.as_view(), name='editar_tabernero'),
    #path('taberneros/delete/<int:pk>/', views.TaberneroDeleteView.as_view(), name='borrar_tabernero'),


    #Clientes Frecuentes
    path('clientes/', views.clientes_frecuentes, name='clientes_frecuentes'),
    path('clientes/<int:cliente_id>/', views.detalle_clientes_frecuentes, name='detalle_clientes'),
    path('clientes/form/', views.clientes_frecuentes_form, name='clientes_form'),
    #path('clientes/list/', views.ClienteFrecuenteListView.as_view(), name='clientes_frecuentes_list'),
    #path('clientes/detail/<int:pk>/', views.ClienteFrecuenteDetailView.as_view(), name='detalle_cliente'),
    #path('clientes/create/', views.ClienteFrecuenteCreateView.as_view(), name='crear_cliente'),
    #path('clientes/update/<int:pk>/', views.ClienteFrecuenteUpdateView.as_view(), name='editar_cliente'),
    #path('clientes/delete/<int:pk>/', views.ClienteFrecuenteDeleteView.as_view(), name='borrar_cliente'),


    # Productos
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('productos/form/', views.productos_form, name='productos_form'),
    path('buscar/', views.buscar_productos, name='buscar_productos'),
    #path('productos/list/', views.ProductoListView.as_view(), name='productos_list'),
    #path('productos/detail/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle_producto'),
    #path('productos/create/', views.ProductoCreateView.as_view(), name='crear_producto'),
    #path('productos/update/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    #path('productos/delete/<int:pk>/', views.ProductoDeleteView.as_view(), name='borrar_producto'),
    #path('productos/buscar/', views.BuscarProductoView.as_view(), name='buscar_producto'),
]