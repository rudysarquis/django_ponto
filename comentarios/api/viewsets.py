from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from comentarios.models import Comentario
from .serializer import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):

    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    #mesma coisa que na versão do app atracoes, diferença que lá esta generico
    # e aqui tem que fazer view a view
    filter_backends = (DjangoFilterBackend)