from rest_framework.viewsets import ModelViewSet
from core.api.serializers import LojistaSerializer


# Viewsets do ecommerce


class LojistaViewset(ModelViewSet):
    """
        A viewset do modelo de Lojista
    """
    serializer_class = LojistaSerializer

    def get_queryset(self):
        lojista = LojistaSerializer.Meta.model
        queryset = lojista.objects.all()

        return queryset