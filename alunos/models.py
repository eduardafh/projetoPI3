from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT)
    data_pedido = models.DateField()
    valor = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cliente.nome}'

class Itens(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    produto = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)
    preco_unitario = models.CharField(max_length=100)

    def __str__(self):
        return self.produto
