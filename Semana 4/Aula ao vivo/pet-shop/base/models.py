from django.db import models

# Modelo de Contato
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.nome} ({self.email})'


# modelo de Petshop
class Petshop(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()


# Modelo de Reserva
class Reserva(models.Model):
    nome_pet = models.CharField(verbose_name='Nome do Pet', max_length=50)
    telefone = models.CharField(max_length=15)
    data_reserva = models.DateField()
    observacoes = models.TextField()
    petshop = models.ForeignKey(
        Petshop, models.SET_NULL, null=True, blank=True, related_name='reservas'
    )
