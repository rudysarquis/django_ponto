from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #mesmo comportamento do queryset declarado na função viewset do core na função get_queryset
    filter_fields = ('nome', 'descricao')
