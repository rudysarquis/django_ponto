from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends  = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    #permission_classes = (IsAuthenticated,)
   # authentication_classes = (TokenAuthentication,)
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset  = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset


    # OVERWRITE THE METODOS DEFAULT DO DJANGO REST FRAMEWORK
    # Método para sobrescrever o GET, se pode fazer o que quiser com o list, retornando um objeto customizavel
    # Funciona para o endpoint como um todo ao contrario do retrieve
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # Metodo utilizado para escrever o verbo POST
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    #Método utilizado para escrever o verbo DELETE | OUTRO fato é acionado para deletar um recurso não o endpoint como um todo
    def destroy(self, request, *args, **kwargs):
        super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    #Funciona para "listar" apenas recursos ao contrario do list
    def retrieve(self, request, *args, **kwargs):
        super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    #Atualiza uma parte do objeto corresponde a PATCH no postman
    def partial_update(self, request, *args, **kwargs):
        super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    #UPDATE o objeto inteiro campo que é retornado do Serielizer corresponde ao PUT
    def update(self, request, *args, **kwargs):
        super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    #Criaando uma action personalizada, no caso de denuncia de um campo que o usuario queira denunciar usando um decaorator
    # detail = True mostra a pk que sera utilizada caso contrario sera do endpoint todo, precisa acessar um recurso em si.
    # passando o
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass