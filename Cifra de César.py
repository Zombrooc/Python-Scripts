#!/usr/bin/python3


alpha = (
            'a', 'b', 'c',
            'd', 'e', 'f', 
            'g', 'h', 'i', 
            'j', 'k', 'l', 
            'm', 'n', 'o', 
            'p', 'q', 'r', 
            's', 't', 'u', 
            'v', 'w', 'x', 
            'y', 'z'
        )


def decode(text, *args):
    descriptedText = ""
    text = text.lower()
    if args:
        base = args[0]
        if base > 26:
            while base > 26:
                base-=26
        for el in text:
            if el not in alpha:
                descriptedText+=el
            else:
                try:
                    nextLetter = alpha.index(el)-base
                    descriptedText+=alpha[nextLetter]
                except IndexError:
                    nextLetter = 26-(alpha.index(el)-base)
                    descriptedText+=alpha[abs(nextLetter)]
        return descriptedText
    else:
        base = 1
        message = {}
        while base <= 26:
            for el in text:
                if el not in alpha:
                    descriptedText+=el
                else:
                    try:
                        nextLetter = alpha.index(el)-base
                        descriptedText+=alpha[nextLetter]
                    except IndexError:
                        nextLetter = 26-(alpha.index(el)-base)
                        descriptedText+=alpha[abs(nextLetter)]
            message[base] = descriptedText
            descriptedText = ""
            base+=1
        return message


def encode(text, base):
    criptedText = ""
    text = text.lower()
    if base > 26:
        while base > 26:
            base-=26
    for el in text:
        if el not in alpha:
            criptedText+=el
        else:
            try:
                nextLetter = alpha.index(el)+base
                criptedText+=alpha[nextLetter]
            except IndexError:
                nextLetter = 26-(alpha.index(el)+base)
                criptedText+=alpha[abs(nextLetter)]
    return criptedText


def init():
    print(' [ 1 ] - Encode ')
    print(' [ 2 ] - Decode ')
    opcao = input('Escolha uma opção: ')
    try:
        opcao = int(opcao)
        if opcao is 1:
            nonCriptedText = input('Digite o texto a ser criptografado: ')
            baseEncode = int(input('Digite uma base de codificação: '))
            print(encode(nonCriptedText, baseEncode))
        elif opcao is 2:
            criptedText = input('Digite o texto a ser descriptografado: ')
            baseDecode = input('Digite uma base de codificação: ')
            if not baseDecode:
                n = decode(criptedText)
                for el in range(1, 27):
                    print('Base {x} = {y}'.format(x=el, y=n[el]))
                init()
            else:
                try:
                    baseDecode = int(baseDecode)
                    print(decode(criptedText, baseDecode))
                    init()
                except ValueError:
                    print('Use apenas números para a base de codificação')
                    init()
        elif opcao is 0:
            exit()
        else:
            print('Digite uma opção válida')
            init()
    except ValueError:
        print('Digite apenas números')
        init()
init()
