from os import system, getlogin, mkdir
from wget import download
from os.path import exists

user = getlogin()
if not exists(f'C:\\Users\\{user}\\TinhaQueSerOCoven'):
    mkdir(f'C:\\Users\\{user}\\TinhaQueSerOCoven')
if not exists(f'C:\\Users\\{user}\\TinhaQueSerOCoven\\the-last-of-us-uncharted-4-co-director-bruce-straley-leaves_3ugj.jpg'):
    url = "https://sm.ign.com/ign_br/news/t/the-last-o/the-last-of-us-uncharted-4-co-director-bruce-straley-leaves_3ugj.jpg"
    filename = download(url)


system('@echo off')
system('REG ADD "HKCU\Control Panel\Desktop" /v wallpaper /t REG_SZ /d "" /f ')
system('REG ADD "HKCU\Control Panel\Desktop" /v wallpaper /t REG_SZ /d "C:\\Users\\{user}\\TinhaQueSerOCoven\\the-last-of-us-uncharted-4-co-director-bruce-straley-leaves_3ugj.jpg" /f ')
system('REG DELETE "HKCU\Software\Microsoft\Internet Explorer\Desktop\General" /v WallpaperSource /f')
system('REG ADD "HKCU\Control Panel\Desktop" /v WallpaperStyle /t REG_SZ /d 2 /f')
system('RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters')