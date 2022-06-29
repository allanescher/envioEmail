## TUTORIAL ENVIO E-MAIL

#### Bibliotecas utilizadas
```bash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
```

#### Inclusão das credenciais
```bash
SENDER_MAIL = ''
SENDER_PASS = ''
```

#### Definição do Provedor de envio de e-mail
```bash
SMTP_PROVIDER = [
    'smtp.office365.com'
]
```

#### Função para informar 
```bash
def writeMail(to, subject, body):
    msg = MIMEMultipart() #Declarando msg
    msg['From'] = 'smtpbpk@outlook.com' #Carregando e-mail que envia irá enviar o e-mail
    msg['To'] = to #Carregando destinário
    msg['Subject'] = subject #Carregando assunto do e-mail
    body = body #Carregando corpo do e-mail
    msg.attach(MIMEText(body, 'plain')) #Informar o tipo de informação a ser enviado, sendo em html ou texto no corpo do e-mail
    #msg.attach(MIMEText(body, 'html'))

    return msg #Retorno da função
```

#### Função para enviar e-mail
```bash
def sendMail(mail, prov):
    p = SMTP_PROVIDER[0] if prov == 'outlook' else SMTP_PROVIDER[1]
    server = smtplib.SMTP(p, 587)  ### put your relevant SMTP here
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SENDER_MAIL, SENDER_PASS)  ### if applicable
    server.send_message(mail)
    server.quit()
```

