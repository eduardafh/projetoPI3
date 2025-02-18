from rest_framework.serializers import ModelSerializer
from .models import Clientes, Pedidos, Itens

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class PedidosSerializer(ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


class ItensSerializer(ModelSerializer):
    class Meta:
        model = Itens
        fields = '__all__'