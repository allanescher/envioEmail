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

#### Função para informar parâmetros ao servidor
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
def sendMail(mail):
    server = smtplib.SMTP(SMTP_PROVIDER, 587)  #Determinação do host e da porta de envio
    server.ehlo()
    server.starttls() #Criptografia para iniciar conexão segura
    server.ehlo()
    server.login(SENDER_MAIL, SENDER_PASS)  #Passagem para o servidor dos parâmetros de envio, como e-mail e senha
    server.send_message(mail) #Passando o e-mail para envio do servidor
    server.quit() #Fechar servidor do e-mail 
```

#### Funcão 
```bash
send_mail = 0 
while send_mail != 2: #While para enviar e-mail
    send_mail = int(input("Deseja 1 para enviar e-mail, digite 2 para sair?\n")) #Variável para prosseguir ou sair do While
    if(send_mail == 1): #Condição para enviar e-mail
        SENDER_MAIL = input('Digite o seu email\n') #Variável para receber o e-mail do remetente
        SENDER_PASS = input('Digite a sua senha\n') #Variável para receber a senha do usuário remetente
        toMail = input('Digite o email do destinatário\n') #Variável para receber o e-mail do destinatário
        subject = input('Digite o titulo do email\n') #Variável para receber o título do e-mail
        body = input('Digite o conteudo do email\n') #Variável para receber o corpo do e-mail
        mail = writeMail(toMail, subject, body, SENDER_MAIL) #Variável que chama função que envia as informações para o servidor
        sendMail(mail) #Função que envia o e-mail
        print('Email enviado com sucesso!!!')
```
