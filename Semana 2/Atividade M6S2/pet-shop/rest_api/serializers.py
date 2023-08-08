from rest_framework.serializers import ModelSerializer

from base.models import Contato, Reserva

class ContatoModelSerializer(ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

class ReservaModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"