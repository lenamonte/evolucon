from django.conf import settings
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=9)
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    respons_direto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self):
        return self.nome

    def update(self, nome, cpf, rg, data_nascimento, endereco, cep, nome_pai, nome_mae, celular):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cep = cep
        self.nome_pai = nome_pai
        self.nome_mae = nome_mae
        self.celular = celular
        self.save()

    def delete(self):
        self.delete()