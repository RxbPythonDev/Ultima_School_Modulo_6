import datetime as dt
from rest_framework import serializers

from base.models import Reserva, Petshop, Categoria

class PetshopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Petshop
        fields = [
            'id',
            'nome',
            'telefone',
            'endereco'
        ]

class CategoriaSerializer(serializers.ModelSerializer):
    reservas = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="api:reserva-detail",
    )
    class Meta:
        model = Categoria
        fields = [
            'id',
            'nome',
            'reservas',
        ]

class ReservaSerializer(serializers.ModelSerializer):

    def validate_data_reserva(self, value):
        if value < dt.date.today():
            raise serializers.ValidationError('A reserva não pode ser feita no passado!')
        return value

    categoria = serializers.SlugRelatedField(slug_field='nome', queryset=Categoria.objects.all())

    class Meta:
        model = Reserva
        fields = [
            'nome_pet',
            'telefone',
            'data_reserva',
            'observacoes',
            'categoria',
        ]
