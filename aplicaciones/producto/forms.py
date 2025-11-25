from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    # Sobrescribimos el constructor para añadir una clase de Bootstrap 
    # a los campos (si planeas usar Bootstrap)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Producto
        # Incluye todos los campos excepto la fecha de registro
        fields = ['nombre', 'categoria', 'sku', 'precio', 'stock']
        # Opcional: Personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'sku': 'Código SKU',
            'precio': 'Precio Unitario',
            'stock': 'Unidades en Stock',
        }