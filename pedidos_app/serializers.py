from rest_framework import serializers
from pedidos_app.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# rellenar después con class ProductoSerializer... CategoriaSerializer, etc