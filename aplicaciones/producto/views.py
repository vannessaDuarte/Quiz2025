from django.shortcuts import render
from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy
from .models import Producto
from aplicaciones.categoria.models import Categoria
from .forms import ProductoForm
# Create your views here.

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/lista_productos.html'
    context_object_name = 'productos'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html' # Usaremos un template genérico
    success_url = reverse_lazy('lista_productos') # Redirigir a la lista al guardar


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html' # Reutilizamos el mismo template de formulario
    success_url = reverse_lazy('lista_productos')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html' # Template para pedir confirmación
    context_object_name = 'producto'
    success_url = reverse_lazy('lista_productos')
