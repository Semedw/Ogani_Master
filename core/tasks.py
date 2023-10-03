from celery import shared_task
from .models import Subscriber
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# test simple task repeat every 10 seconds with crontab

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active=True).values_list('email',flat=True)
    mail_text = f"Salam, <br> Bu sadece bir test emailidir, narahat olma <br> Diqqetin ucun tesekkur, <br> <h1>Semed</h1>"

    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()