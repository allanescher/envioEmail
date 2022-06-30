
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#SENDER_MAIL = 'smtpbpk@outlook.com'
#SENDER_PASS = 'smtpbiopark01'

SMTP_PROVIDER = 'smtp.office365.com'


def writeMail(to, subject, body, email):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))

    return msg

def sendMail(mail):
    server = smtplib.SMTP(SMTP_PROVIDER, 587)  ### put your relevant SMTP here
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SENDER_MAIL, SENDER_PASS)  ### if applicable
    server.send_message(mail)
    server.quit()

send_mail = 0
while send_mail != 2:
    send_mail = int(input("Deseja 1 para enviar e-mail, digite 2 para sair?\n"))
    if(send_mail == 1):
        SENDER_MAIL = input('Digite o seu email\n')
        SENDER_PASS = input('Digite a sua senha\n')
        toMail = input('Digite o email do destinatário\n')
        subject = input('Digite o titulo do email\n')
        body = input('Digite o conteudo do email\n')
        mail = writeMail(toMail, subject, body, SENDER_MAIL)
        sendMail(mail)
        print('Email enviado com sucesso!!!')
