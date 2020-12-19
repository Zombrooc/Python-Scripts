from os import system


def Soma():
    Valores_Linhas = []
    N_matrizes = int(input('Digite o número de Matrizes: '))
    Linhas = int(input('Digite o número de Linhas: '))
    Colunas = int(input('Digite o número de Colunas: '))
    for Matriz in range(N_matrizes):
        for Linha in range(Linhas):
            for Coluna in range(Colunas):
                Linha = Linha+1
                Coluna = Coluna+1
                Valor = float(input(f'Digite o valor da Linha {Linha}, Coluna {Coluna}: '))
                Valores_Linhas.append(Valor)
    


def inicio():
    while True:
        print('[ 1 ] - Soma')
        print('[ 2 ] - Multiplicação')
        print('[ 3 ] - Divisão')
        print('[ 4 ] - Derterminante')
        print('[ 5 ] - Limpar Prompt')
        opcao = input('Digite uma opção:  ')
        try:
            opcao = int(opcao)
            if opcao == 1:
                Soma()
            elif opcao == 2:
                ...
            elif opcao == 3:
                ...
            elif opcao == 4:
                ...
            elif opcao == 5:
                system('cls')
            else:
                print('Digite uma opção válida...')
        except ValueError:
            print('Digite apenas Número...')


inicio()