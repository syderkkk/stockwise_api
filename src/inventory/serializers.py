from rest_framework import serializers
from .models import Producto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    # Punto adicional: Personaliza la respuesta mostrando campos completos de la categoría relacionada
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'cantidad', 'precio', 'categoria', 'categoria_detalle']