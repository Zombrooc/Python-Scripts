from random import randrange
from time import sleep


cpf = []


def aleatorio(cpf):
    i=1
    while i<10:
        n = randrange(10)
        cpf.append(n)
        i+=1
    calculo_1(cpf)
    print(str(cpf)[1::3])
    sleep(2)
    inicio()


def calculo_1(cpf):
    i = 0
    modulo = 0
    j = 10
    soma = 0
    cpf2 = str(cpf)[1::3]
    tam = len(cpf)
    for num in range(tam):
        x = int(cpf2[num])*j
        soma = soma + x
        j-=1
    if soma%11 <= 2:
        cpf.append(0)
    else:
        modulo = 11-(soma%11)
        cpf.append(modulo)
    calculo_2(cpf)


def calculo_2(cpf):
    i = 0
    modulo = 0
    j = 11
    soma = 0
    cpf2 = str(cpf)[1::3]
    tam = len(cpf)
    for num in range(tam):
        x = int(cpf2[num])*j
        soma = soma + x
        j-=1
    if soma%11 <= 2:
        cpf.append(0)
    else:
        modulo = 11-(soma%11)
        cpf.append(modulo)


def digita():
    cpf_user = input('Digite 9 Digitos para serem calculados: ')
    for n in cpf_user:
        cpf.append(int(n))
    calculo_1(cpf)
    print(str(cpf)[1::3])
    sleep(2)
    inicio()


def inicio():
    cpf = []
    print('[ 1 ] CPF aleatório')
    print('[ 2 ] Digite um número')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        aleatorio(cpf)
    elif opcao == 2:
        digita()


inicio()
