from django.urls import path

from rest_framework.routers import SimpleRouter

from rest_api.views import inicio, ReservaViewSet, PetshopViewSet, CategoriaViewSet

router = SimpleRouter(trailing_slash=False)
router.register('reservas', ReservaViewSet, basename='reserva')
router.register('petshops', PetshopViewSet, basename='petshop')
router.register('categorias', CategoriaViewSet, basename="categoria")

app_name = 'rest_api'

urlpatterns = [
    path('', inicio, name='inicio'),
] + router.urls
