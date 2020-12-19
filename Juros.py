from time import sleep

def juros_simples(i, C, t):
    i = i/100
    j = (i*C)
    print(f'Juros obtidos no fim do primeiro período: {j}')
    print(f'Juros obtidos no final de {t} Perídos: {j*t}')
    M = C + (j*t)
    print(f'Montante: {M}\n')
    sleep(2)
    inicio()

def juros_composto(i, C, t):
    i = i/100
    M = C*(1+i)**t
    print()
    print(f'Montante: {M}')
    j = M - C
    
    print(f'Juros {j}\n')
    sleep(2)
    inicio()

def taxa_juros_simples(C, t, j):
    i = (j/(C*t))*100
    print(f'{i}')
    sleep(2)
    inicio()

def inicio():
    print(' [ 1 ] Descobrir Montante (Juros Simples) ')
    print(' [ 2 ] Descobrir Montante (Juros Composto)')
    print(' [ 3 ] Descobrir Taxa de Juros Simples')
    try:
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            taxa = float(input('Digite a taxa de juros: '))
            capital = float(input('Digite o capital: '))
            tempo = int(input('Digite o tempo: '))
            juros_simples(taxa, capital, tempo)
        elif opcao == 2:
            taxa = float(input('Digite a taxa de juros: '))
            capital = float(input('Digite o capital: '))
            tempo = int(input('Digite o tempo: '))
            juros_composto(taxa, capital, tempo)
        elif opcao == 3:
            capital = float(input('Digite o capital: '))
            tempo = int(input('Digite o tempo: '))
            juros = float(input('Digite o valor dos juros: '))
            taxa_juros_simples(capital, tempo, juros)
        else:
            print('Digite uma opção válida...')
            inicio()
    except ValueError:
        print('Digite apenas números...')
        inicio();
inicio()
