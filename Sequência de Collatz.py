from time import sleep
from os import system
from sys import exit

def collatz(num):
    while num != 1:
        if num%2 == 0:
            num = num//2
            print(f'{num}\n')
        elif num%2 != 0:
            num = 3*num+1
            print(f'{num}\n')
    sleep(2)


while True:
    print('[ 1 ] Sequência de Collatz')
    print('[ 2 ] Limpar Prompt')
    print('[ 3 ] Sair')
    opcao = input('Digite uma opção: ')
    try:
        opcao = int(opcao)
        if opcao == 1:
            n = int(input('Digite um número: '))
            collatz(n)
        elif opcao == 2:
            system('cls')
        elif opcao == 3:
            exit()
        else:
            print('Digite uma opção válida...')
    except ValueError:
        print('Digite apenas números....')

