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
def writeMail(to, subject, body, email):
    msg = MIMEMultipart() #Declarando msg
    msg['From'] = email #Carregando e-mail que envia irá enviar o e-mail
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
    p = SMTP_PROVIDER[0] if prov == 'outlook' else SMTP_PROVIDER[1] #Condição para enviar e-mail pelo provedor outlook
    server = smtplib.SMTP(p, 587)  #Determinação do host e da porta de envio
    server.ehlo()
    server.starttls() #Criptografia para envio de e-mail
    server.ehlo()
    server.login(SENDER_MAIL, SENDER_PASS)  #Passagem para o servidor dos parâmetros de envio, como e-mail e senha
    server.send_message(mail) #Passando o e-mail para envio do servidor
    server.quit() #Fechar servidor do e-mail 
```

#### Funcão 
