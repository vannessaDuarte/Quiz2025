from django.views.generic import CreateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Categoria
from .forms import CategoriaForm

class CategoriaCreateAjaxView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'catalogos/categoria_form.html'
    success_url = reverse_lazy('lista_productos') # URL de fallback

    def form_valid(self, form):
        # Guarda el objeto de categoría
        self.object = form.save()
        
        # 1. Si la solicitud es AJAX (lo que esperamos desde el modal):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Devuelve los datos de la nueva categoría en formato JSON
            return JsonResponse({
                'success': True,
                'id': self.object.id,
                'nombre': self.object.nombre
            })
        
        # 2. Si no es AJAX (acceso directo), redirige normalmente
        return super().form_valid(form)

    def form_invalid(self, form):
        # Si la solicitud es AJAX y el formulario es inválido, 
        # devolvemos el formulario con errores en HTML para que el modal lo muestre.
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors})

        return super().form_invalid(form)
