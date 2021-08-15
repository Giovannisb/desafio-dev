from django.db import models

# Create your models here.
class Arquivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    data_upload = models.DateTimeField()


class Tipo(models.Model):
    id = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=25)
    natureza = models.CharField(max_length=25)
    sinal = models.CharField(max_length=2)


class Cnae(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_arquivo = models.IntegerField()
    tipo = models.CharField(max_length=20)
    data = models.DateField()
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=10, default='')
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
    operacao = models.CharField(max_length=2, default='')
