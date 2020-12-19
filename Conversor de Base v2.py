def Dec_to_Other(dec):
    decimal = dec
    hexadecimal = hex(dec)[2:].upper()
    octal = oct(dec)[2:]
    binario = bin(dec)[2:]
    return decimal, hexadecimal, octal, binario


def inicio():
    print(' [ 1 ] - Decimal')
    print(' [ 2 ] - Hexadecimal')
    print(' [ 3 ] - Octal')
    print(' [ 4 ] - Binário')
    opcao = int(input('Digite uma opção: '))
    opcao2 = int(input('Digite a segunda opção: '))
    numero = input('Digite o número a ser convertido: ')
    
    #Converter Decimal para as 
    #demais bases Decimais
    if opcao == 1:
        numero = int(numero)
        decimal = Dec_to_Other(numero)
        
        if opcao2 == 1: #--------> Decimal para Decimal
            print(decimal[0])
        
        elif opcao2 == 2: #--------> Decimal para Hexadecimal
            print(decimal[1])
        
        elif opcao2 == 3: #-------> Decimal para Octal
            print(decimal[2])
        
        elif opcao2 == 4: #-----> Decimal para Binário
            print(decimal[3])
    
    #Converter Hexadecimal para as demais bases
    elif opcao == 2:
        p = numero
        p = p[::-1]
        tam = len(p)
        decimal = 0
        for algo in range(tam):
            p = str(p)
            p = p.upper()
            if p[algo] == 'A':
                decimal = decimal + (10*(16**algo))
            elif p[algo] == 'B':
                decimal = decimal + (11*(16**algo))
            elif p[algo] == 'C':
                decimal = decimal + (12*(16**algo))
            elif p[algo] == 'D':
                decimal = decimal + (13*(16**algo))
            elif p[algo] == 'E':
                decimal = decimal + (14*(16**algo))
            elif p[algo] == 'F':
                decimal = decimal + (15*(16**algo))
            else:
                p1 = int(p[algo])
                resultado = p1 * (16 ** algo)
                decimal = decimal + resultado
        decimal = Dec_to_Other(decimal)
        if opcao2 == 1: #--------> Decimal para Decimal
            print(decimal[0])
        
        elif opcao2 == 2: #--------> Decimal para Hexadecimal
            print(decimal[1])
        
        elif opcao2 == 3: #-------> Decimal para Octal
            print(decimal[2])
        
        elif opcao2 == 4: #-----> Decimal para Binário
            print(decimal[3])
    

    #Converter Octal para as demais bases
    elif opcao == 3:
        p = numero
        tam = len(p)
        p = p[::-1]
        decimal = 0
        for algo in range(tam):
            decimal = decimal + int(p[algo]) * (8 ** algo)
        decimal = Dec_to_Other(decimal)
        if opcao2 == 1: #--------> Decimal para Decimal
            print(decimal[0])
        
        elif opcao2 == 2: #--------> Decimal para Hexadecimal
            print(decimal[1])
        
        elif opcao2 == 3: #-------> Decimal para Octal
            print(decimal[2])
        
        elif opcao2 == 4: #-----> Decimal para Binário
            print(decimal[3])
    
    
    #Converter Binário para as demais bases
    elif opcao == 4:
        numero = numero[::-1]
        tam = len(numero)
        decimal = 0
        for num in range(tam):
            if numero[num] == "1":
                decimal = decimal + (2**num)
        decimal = Dec_to_Other(decimal)
        if opcao2 == 1: #--------> Decimal para Decimal
            print(decimal[0])
        
        elif opcao2 == 2: #--------> Decimal para Hexadecimal
            print(decimal[1])
        
        elif opcao2 == 3: #-------> Decimal para Octal
            print(decimal[2])
        
        elif opcao2 == 4: #-----> Decimal para Binário
            print(decimal[3])
        


inicio()

    

    
