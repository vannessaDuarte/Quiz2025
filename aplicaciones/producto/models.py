from django.db import models
from aplicaciones.categoria.models import *

# Modelo para los productos individuales
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    # Clave Foránea a Categoria. on_delete=models.CASCADE significa que si la categoría se elimina,
    # todos sus productos asociados también se eliminan.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    sku = models.CharField(max_length=50, unique=True) # Stock Keeping Unit
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.sku})"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
