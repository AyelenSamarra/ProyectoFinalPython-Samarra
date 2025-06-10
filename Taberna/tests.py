from django.test import TestCase
from .models import *

# Create your tests here.
class ModeloTest(TestCase):
    def setUp(self):
        Tabernero.objects.create(nombre="Juan", apellido="Perez", edad=30)
        ClienteFrecuente.objects.create(nombre="Ana", apellido="Gomez", pedido_favorito="Cerveza")
        Producto.objects.create(nombre="Cerveza", precio="5.00", stock=100)

        def test_tabernero_str(self):
            tabernero = Tabernero.objects.get(nombre="Juan")
            self.assertEqual(str(tabernero), "Juan Perez")
        def test_cliente_frecuente_str(self):
            cliente = ClienteFrecuente.objects.get(nombre="Ana")
            self.assertEqual(str(cliente), "Ana Gomez")
        def test_producto_str(self):
            producto = Producto.objects.get(nombre="Cerveza")
            self.assertEqual(str(producto), "Cerveza - $5.00")