from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.listar_productos),
    path('products/create/', views.crear_producto),
    path('products/edit/<int:id>/', views.editar_producto),
    path('products/delete/<int:id>/', views.eliminar_producto),
]