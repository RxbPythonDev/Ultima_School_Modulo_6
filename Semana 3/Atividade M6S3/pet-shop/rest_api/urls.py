from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import inicio, ReservaViewSet

router = SimpleRouter(trailing_slash=False)
router.register('reservas', ReservaViewSet, basename='reserva')

app_name = 'rest_api'

urlpatterns = [
    path('', inicio, name='inicio'),
] + router.urls
