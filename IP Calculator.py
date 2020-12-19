import time
import sys

def calculo(p):
    i = 0
    while True:
        if ((2**i)-2) >= p:
            subrede = 256-2**i
            return subrede
            break
        else:
            i+=1


def numsubrede(p):
    bin = dec_to_bin(p)
    bit1 = 0
    for n in bin:
        if n == '1':
            bit1 += 1
    numero_de_subs = 2**bit1
    return numero_de_subs
            
            
def numip(p):
    bin = dec_to_bin(p)
    bit0 = 0
    for n in bin:
        if n == '0':
            bit0 += 1
    num_ip = 2**bit0
    return num_ip
     
               
def dec_to_bin(p):
    p = calculo(p)
    binario = ""
    while p >= 1:
        binario = (binario + str(int(p % 2)))
        p = p//2
    binario = binario[::-1]
    return binario


def main():
    print ('Calculadora de IP Classe C')
    try:
        p = int(input('Digite o número de dispositivos na rede: '))
        if p != 0:
            print('Mascara de Sub-rede: 255.255.255.',calculo(p))
            print('Numero de Sub-redes: ', numsubrede(p))
            print('Numero de IPs por Sub-rede: ', numip(p))
            numipv = int(numip(p)) - 2
            print('Numero de IPs válidos: {}\n'.format(numipv))
            time.sleep(5)
            main()
        else:
             sys.exit()
    except ValueError:
        print('Digite apenas números...')
        main()

main()