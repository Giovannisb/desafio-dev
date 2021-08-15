# -*- coding: utf-8 -*-
import json
from datetime import datetime
from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import *

def identifica_tipo(t):
    tipo = Tipo.objects.filter(id=t).values_list('descricao', 'sinal')
    descricao = tipo[0][0]
    sinal = tipo[0][1]

    return descricao, sinal
def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        data = datetime.now()
        arquivo = Arquivo(nome=filename, data_upload=data)
        arquivo.save()

        f = Arquivo.objects.filter(nome=filename).values_list('id', 'nome')
        id = f[0][0]
        arq = fs.open(filename)
        linhas = arq.readlines()
        for linha in linhas:
            linha = linha.decode("utf-8")
            print(linha)
            t = linha[0]
            tipo, sinal = identifica_tipo(t)
            data = linha[1:9]
            valor = int(linha[9:18])
            val = valor/100
            cpf = linha[19:30]
            cartao = linha[30:42]
            horario = linha[42:48]
            dono = linha[48:62]
            loja = linha[62:80]

            ano = data[:4]
            mes = data[5:6]
            dia = data[7:]
            str_data = ano + '-' + mes + '-' + dia
            data = datetime.strptime(str_data, '%Y-%m-%d').date()

            hora = horario[0:2]
            minuto = horario[2:4]
            segundo = horario[4:]
            str_horario = hora + ':' + minuto + ':' + segundo

            if sinal == '+':
                val = val
            else:
                val = val * (-1)

            cnae = Cnae(id_arquivo=id, tipo=tipo, data=data, valor=val, cpf=cpf, cartao=cartao,
                        hora=str_horario, dono_loja=dono, nome_loja=loja, operacao=sinal)
            cnae.save()
            obj = Cnae.objects.all()
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url,
            'cnae': obj
        })

    else:
        cnae = Cnae.objects.all()
        return render(request, 'index.html', {'cnae': cnae})

def saldos(request):
    cnae = Cnae.objects.all().values('nome_loja', 'dono_loja', 'cpf', 'valor', 'operacao')

    df =pd.DataFrame.from_records(cnae)
    if df.shape[0] == 0:
        tabela = [{'index': 0, 'Loja': '', 'Dono': '', 'CPF': '', 'Saldo':''}]
        return render(request, 'saldos.html', {'tabela': tabela})

    cpf = df.copy()
    cpf.drop_duplicates(subset=['cpf'], inplace=True)
    lista_cpf = cpf.cpf.to_list()
    total = pd.DataFrame(columns=['Loja', 'Dono', 'CPF', 'Saldo'])

    for cpf in lista_cpf:
        x = df.loc[df.cpf == cpf]
        saldo = x.valor.sum()
        y = x.values.tolist()
        data = {
            'Loja': [y[0][0]],
            'Dono': [y[0][1]],
            'CPF': [cpf],
            'Saldo': saldo
        }

        dados = pd.DataFrame.from_dict(data=data)
        total = pd.concat([total, dados], ignore_index=True)
        table = total.reset_index().to_json(orient='records')
        tabela = []
        tabela = json.loads(table)
    return render(request, 'saldos.html', {'tabela': tabela})
