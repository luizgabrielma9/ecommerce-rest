from django.contrib import admin
from .models import Lojista, Produto, Estoque

# Register your models here.

@admin.register(Lojista)
class LojistaModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'endereco_web', 'data_cadastro']


@admin.register(Produto)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_cadastro']


@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['produto', 'lojista', 'quantidade', 'preco_unitario']


