import smtplib
import ssl
from email.message import EmailMessage

listaCorreos = ["carlos98frances@gmail.com","molins.carmen01@gmail.com","joseramonfran@gmail.com","berro.hermida@gmail.com"]

def enviar_correo(correo_destino):
    email_sender = 'carlos98frances@gmail.com'
    email_password = '100sanch100'
    email_receiver = correo_destino

    subject = 'Puntua a tus profesores'
    body = """
    Pulsa en este link para acceder a mi formulario: \n\nhttps://docs.google.com/forms/d/e/1FAIpQLSfreWHn6Wsi4Y2CZ_J73J06eQ_IpBEl9sQt8-7f5rpTtV-LmA/viewform?usp=sf_link
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        
#for correo in listaCorreos:
enviar_correo("carlos98frances@gmail.com")
