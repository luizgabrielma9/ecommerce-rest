from rest_framework.serializers import ModelSerializer
from core.models import Lojista, Produto


# Serializadores do ecommerce


class LojistaSerializer(ModelSerializer):
    """
    Um serializador do modelo Lojista
    """
    class Meta:
        model = Lojista
        fields = [
            'id',
            'nome',
            'telefone',
            'endereco_web',
            'data_cadastro',
        ]
        read_only_fields = ['data_cadastro',]


class ProdutoSerializer(ModelSerializer):
    """
    Um serializador do modelo Produto
    """
    lojistas = LojistaSerializer(many=True)
    
    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'lojistas',
            'data_cadastro',
        ]
        read_only_fields = ['data_cadastro',]


