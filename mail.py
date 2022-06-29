import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

SENDER_MAIL = 'smtpbpk@outlook.com'
SENDER_PASS = 'smtpbiopark01'

SMTP_PROVIDER = [
    'smtp.office365.com'
]

def writeMail(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = 'smtpbpk@outlook.com'
    msg['To'] = to
    msg['Subject'] = subject
    body = body
    msg.attach(MIMEText(body, 'plain'))
    #msg.attach(MIMEText(body, 'html'))

    return msg

def sendMail(mail, prov):
    p = SMTP_PROVIDER[0] if prov == 'outlook' else SMTP_PROVIDER[1]
    server = smtplib.SMTP(p, 587)  ### put your relevant SMTP here
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SENDER_MAIL, SENDER_PASS)  ### if applicable
    server.send_message(mail)
    server.quit()


send_mail = input("Deseja enviar e-mail, digite 1 para envio?\n")
if(send_mail == '1'):
    toMail = "rodolfo_xz@hotmail.com"  #input('Digite seu email\n')
#    body = """\
#        <table>
#            <tr>
#                <th>Título</th><th>Ano</th><th>Metascore</th><th>User score</th><th># votos</th>
#            </tr>
#        """
    body = "Aqui vai seu conteúdo\n\n"
    count = 1
    body += "Parabéns, você conseguiu enviar e-mail."
    mail = writeMail(toMail, 'Envio e-mail', body)
    sendMail(mail, 'outlook')
