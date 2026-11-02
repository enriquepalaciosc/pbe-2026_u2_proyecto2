from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from pedidos_app.models import Cliente
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
def modificar_cliente(request, id):
    try:
        cliente_seleccionado = Cliente.objects.get(id=id)
        serializado = ClienteSerializer(cliente_seleccionado, data=request.data) # request.data = datos modificados desde frontend

        if serializado.is_valid(): # Verifica si cumple con los datos básicos
            serializado.save()
            return Response(serializado.data, status=status.HTTP_202_ACCEPTED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def borrar_cliente(request, id):
    try:
        cliente_obtenido = Cliente.objects.get(id=id)
        cliente_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def listar_clientes(request):
    try:
        listado_clientes = Cliente.objects.all()  # SELECT * FROM cliente;
        serializado = ClienteSerializer(listado_clientes, many=True)  # Convertimos a JSON

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def listar_cliente(request, id):
    try:
        cliente_obtenido = Cliente.objects.get(id=id)
        serializado = ClienteSerializer(cliente_obtenido, many=False) # Al ser 1 resultado es many=False

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


