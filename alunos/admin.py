from django.contrib import admin

# Register your models here.
from .models import Clientes, Pedidos, Itens

admin.site.register(Clientes)

admin.site.register(Pedidos)

admin.site.register(Itens)
