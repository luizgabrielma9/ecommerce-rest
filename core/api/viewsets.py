from rest_framework.viewsets import ModelViewSet
from core.api.serializers import LojistaSerializer, ProdutoSerializer, \
    EstoqueSerializer


# Viewsets do ecommerce


class LojistaViewset(ModelViewSet):
    """
    A viewset do modelo de Lojista
    """
    serializer_class = LojistaSerializer

    def get_queryset(self):
        classe_lojista = LojistaSerializer.Meta.model
        queryset = classe_lojista.objects.all()

        return queryset


class ProdutoViewset(ModelViewSet):
    """
    A viewset do modelo de Produto
    """
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        classe_produto = ProdutoSerializer.Meta.model
        queryset = classe_produto.objects.all()

        return queryset


class EstoqueViewset(ModelViewSet):
    """
    A viewset do modelo de Estoque
    """
    serializer_class = EstoqueSerializer
    search_fields = ['produto__nome',]
    
    def get_queryset(self):
        classe_estoque = self.serializer_class.Meta.model

        # Busca apenas os produtos com pelo menos um item no
        # estoque
        queryset = classe_estoque.objects.filter(quantidade__gt=0)

        # Filtrando os resultados de acordo com os parâmetros
        # da requisição
        termo_busca_produto = self.request.query_params.get('produto', None)
        preco_maximo = self.request.query_params.get('preco_max', None)
        ordenar_preco_crescente = self.request.query_params.get('crescente', None)

        if termo_busca_produto:
            queryset = queryset.filter(produto__nome__icontains=termo_busca_produto)
        if preco_maximo:
            queryset = queryset.filter(preco_unitario__lte=preco_maximo)
        if ordenar_preco_crescente == 'true':
            queryset = queryset.order_by('preco_unitario')

        print('*************************')
        print(self.request.query_params)
        print('*************************')

        return queryset


