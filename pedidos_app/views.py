from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pedidos_app.serializers import ClienteSerializer


# Create your views here.
@api_view(['POST','PUT'])
def crear_cliente(request):
    datos_cliente_deserializado = ClienteSerializer(data=request.data)

    if datos_cliente_deserializado.is_valid(): # Validar básico
        datos_cliente_deserializado.save() # Guardar
        return Response(datos_cliente_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(datos_cliente_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def modificar_cliente(request):
    pass

@api_view(['DELETE'])
def borrar_cliente(request):
    pass

@api_view(['GET'])
def listar_clientes(request):
    pass

@api_view(['GET'])
def listar_cliente(request):
    pass