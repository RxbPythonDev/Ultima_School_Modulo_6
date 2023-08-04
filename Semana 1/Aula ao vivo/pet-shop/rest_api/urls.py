from django.urls import path

from rest_api.views import inicio, reservas

app_name = 'rest_api'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reservas/', reservas, name='reservas'),
]
