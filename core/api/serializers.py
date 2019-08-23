from rest_framework.serializers import ModelSerializer
from core.models import Lojista


# Serializadores do ecommerce


class LojistaSerializer(ModelSerializer):
    """
        Um serializador do modelo Lojista
    """
    class Meta:
        model = Lojista
        fields = [
            'nome',
            'telefone',
            'endereco_web',
            'data_cadastro',
        ]
        read_only_fields = ['data_cadastro',]
