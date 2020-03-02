from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField(read_only=True)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa'
        )
        read_only_fields = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto ):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
        return ponto



    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)



    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
