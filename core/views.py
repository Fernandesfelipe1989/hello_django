from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request, nome, primeiro,segundo):
    if nome == "soma":
        simbol = '+'
        result = primeiro+segundo
    if nome =="multiplicacao":
        simbol = 'x'
        result = primeiro*segundo
    if nome == "subtrair":
        simbol = '-'
        result = primeiro - segundo
    if nome == "divisao":
        simbol = '/'
        if segundo != 0:

            result = primeiro/segundo
        else:
            result = "Erro: divisão por zero"
    return HttpResponse('<h1>A operação de {}:{} {} {} = {} </h1>'.format(nome, primeiro, simbol,segundo, result))
