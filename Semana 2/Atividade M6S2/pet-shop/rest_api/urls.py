from django.urls import path

from rest_api.views import inicio, reservas, ContatoModelViewSet, ReservaModelViewSet

from rest_framework.routers import SimpleRouter

app_name = 'rest_api'

router = SimpleRouter(trailing_slash=False)
router.register("contato", ContatoModelViewSet)
router.register('reserva', ReservaModelViewSet)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reservas/', reservas, name='reservas'),
]

urlpatterns += router.urls