from rest_framework.viewsets import ModelViewSet
from core.api.serializers import LojistaSerializer, ProdutoSerializer


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


