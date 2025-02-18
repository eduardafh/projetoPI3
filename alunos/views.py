from rest_framework.viewsets import ModelViewSet
from .models import Clientes, Pedidos, Itens
from .serializers import ClientesSerializer, PedidosSerializer, ItensSerializer

class ClientesViewSet(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class PedidosViewSet(ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

class ItensViewSet(ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer