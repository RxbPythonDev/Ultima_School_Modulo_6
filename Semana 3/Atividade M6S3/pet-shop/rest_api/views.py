import json
import datetime as dt

from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from base.models import Reserva

from rest_api.serializers import ReservaSerializer

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

'''
/api/reservas - GET (listar)
/api/reservas - POST (criar)
/api/reservas/1 - GET (detalhar)
/api/reservas/1 - DELETE (apagar)
/api/reservas/1 - PUT (atualizar totalmente)
/api/reservas/1 - PATCH (atualizar parcialmente)
'''

class ReservaViewSet(ModelViewSet):

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
