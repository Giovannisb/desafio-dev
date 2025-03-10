# Generated by Django 3.2.6 on 2021-08-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('data_upload', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cnae',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('id_arquivo', models.IntegerField()),
                ('tipo', models.CharField(max_length=20)),
                ('data', models.DateField()),
                ('valor', models.FloatField()),
                ('cpf', models.CharField(max_length=11)),
                ('cartao', models.CharField(max_length=12)),
                ('hora', models.CharField(default='', max_length=10)),
                ('dono_loja', models.CharField(max_length=14)),
                ('nome_loja', models.CharField(max_length=19)),
                ('operacao', models.CharField(default='', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=25)),
                ('natureza', models.CharField(max_length=25)),
                ('sinal', models.CharField(max_length=2)),
            ],
        ),
    ]
