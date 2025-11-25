from django.urls import path
from .views import CategoriaCreateAjaxView

urlpatterns = [
    path('crear-categoria/', CategoriaCreateAjaxView.as_view(), name='crear_categoria'),
]