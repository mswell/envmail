import os
import smtplib
import glob
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders


def enviar_correo(para, assunto, mensagem, anexo):

    msg = MIMEMultipart()
    msg['From'] = 'seu endereço de email'
    msg['To'] = para
    msg['Subject'] = assunto
    if mensagem != '':
        msg.attach(MIMEText(mensagem))
    part = MIMEBase('application', 'octet-stream')
    if anexo != '':
        part.set_payload(open(anexo, 'rb').read())
        part.add_header('Content-Disposition', 'attachment; filename="%s"' %
                        os.path.basename(anexo))
        msg.attach(part)
    Encoders.encode_base64(part)
    #nesse caso estou usando gmail
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(msg['From'], 'SUASENHA')
    mailServer.sendmail(msg['From'], para, msg.as_string())
    mailServer.close()
    print 'Correio enviado'
# Localizando o Anexo
# exemplo Localizando PDF na pasta que esta o código
# arquivo = glob.glob('*.pdf')
# Exemplo para enviar correio sem mensagem e sem anexo
#enviar_correo('Destinatario', 'assunto', '', '')
# Exemplo para enviar correio com mensagem e com anexo
#enviar_correo('Destinatario', 'Assunto',
#              'Corpo do email',
#              '%s' % arquivo[0])
