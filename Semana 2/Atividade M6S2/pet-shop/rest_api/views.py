import json
import datetime as dt
from django.http import HttpResponse
from base.models import Reserva, Contato

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from rest_api.serializers import ContatoModelSerializer, ReservaModelSerializer

def inicio(request):
    reservas = Reserva.objects.all()
    dados = []
    for reserva in reservas:
        dados.append({
            'id': reserva.id,
            'nome_pet': reserva.nome_pet,
            'telefone': reserva.telefone,
            'data_reserva': reserva.data_reserva.strftime('%d/%m/%Y'), # 03/08/2023
            'observacoes': reserva.observacoes,
        })
    return HttpResponse(json.dumps(dados))


@api_view(['GET', 'POST'])
def reservas(request):
    if request.method == 'POST':
        dados = request.data
        nome_pet = dados['nome_pet']
        telefone = dados['telefone']
        data_reserva = dt.datetime.strptime(dados['data_reserva'], '%d/%m/%Y').date()
        observacoes = dados['observacoes']
        reserva = Reserva.objects.create(
            nome_pet=nome_pet, telefone=telefone, data_reserva=data_reserva, observacoes=observacoes
        )
        dados_reserva = {
            'id': reserva.id,
            'nome_pet': reserva.nome_pet,
            'telefone': reserva.telefone,
            'data_reserva': reserva.data_reserva,
            'observacoes': reserva.observacoes,
        }
        return Response(dados_reserva)
    else:
        reservas = Reserva.objects.all()
        dados = []
        for reserva in reservas:
            dados.append({
                'id': reserva.id,
                'nome_pet': reserva.nome_pet,
                'telefone': reserva.telefone,
                'data_reserva': reserva.data_reserva,
                'observacoes': reserva.observacoes,
            })
        return Response(dados)

class ContatoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoModelSerializer

class ReservaModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaModelSerializer