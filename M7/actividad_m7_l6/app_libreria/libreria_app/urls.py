from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_libros),
    path('libros/crear/', views.crear_libro),
    path('libros/editar/<int:id>/', views.editar_libro),
    path('libros/eliminar/<int:id>/', views.eliminar_libro),
]