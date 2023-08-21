import datetime as dt
from rest_framework import serializers

from base.models import Reserva


class ReservaSerializer(serializers.ModelSerializer):

    def validate_data_reserva(self, value):
        if value < dt.date.today():
            raise serializers.ValidationError('A reserva não pode ser feita no passado!')
        return value
    
    class Meta:
        model = Reserva
        fields = [
            'id',
            'nome_pet',
            'telefone',
            'data_reserva',
            'observacoes',
        ]
