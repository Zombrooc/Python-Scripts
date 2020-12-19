from shutil import copy2, move
from sys import exit
from datetime import datetime
from os import walk, mkdir, chdir, system, getlogin
from os.path import exists
from time import sleep


def backup():
    system('cls')
    print('Processando...')
    user = getlogin()
    now = datetime.now()
    tempo = f'{now.year}-{now.month}-{now.day} - {now.hour}h{now.minute}'
    jpg = 1
    png = 1
    if not exists(f'C:\\Backup {tempo}'):
        mkdir(f'C:\\Backup {tempo}')
    chdir('C:/Users/')
    for root, dirs, files in walk('.', topdown=False):
        caminho = root[2:]
        for nome in files:
            if nome.endswith('.jpg'):
                if not exists(f'C:\\Backup {tempo}\\JPG'):
                    mkdir(f'C:\\Backup {tempo}\\JPG')
                else:
                    extensao = '.jpg'
                    destino = f'C:\\Backup {tempo}\\JPG\\{jpg}{extensao}'
                    try:
                        arquivo = f'C:\\Users\\{caminho}\\{nome}'
                        copy2(arquivo, destino)
                    except:
                        continue
                    jpg += 1
            elif nome.endswith('.png'):
                if not exists(f'C:\\Backup {tempo}\\PNG'):
                    mkdir(f'C:\\Backup {tempo}\\PNG')
                else:
                    extensao = '.png'
                    destino = f'C:\\Backup {tempo}\\PNG\\{png}{extensao}'
                    try:
                        arquivo = f'C:\\Users\\{caminho}\\{nome}'
                        copy2(arquivo, destino)
                    except:
                        continue
                    png += 1
            elif nome.endswith('.zip'):
                if not exists(f'C:\\Backup {tempo}\\ZIP'):
                    mkdir(f'C:\\Backup {tempo}\\ZIP')
                else:
                    destino = f'C:\\Backup {tempo}\\ZIP\\{nome}'
                    try:
                        arquivo = f'C:\\Users\\{caminho}\\{nome}'
                        copy2(arquivo, destino)
                    except:
                        continue
    move(f'C:\\Backup {tempo}', f'C:\\Users\\{user}\\Desktop')
    sair = input('Backup Concluido\nPRECIONE QUALQUER TECLA PARA SAIR...')
    if len(sair)>=0:
        exit()


iniciar = input(f'O Backup de seus arquivos será armazenado em uma pasta no Desktop da sua máquina nomeada com a data e hora de Backup, assim que concluído o software irá exibir uma mesangem de conslusão. ')
if len(iniciar)>=0:
    print('Iniciando...')
    sleep(5)
    backup()
