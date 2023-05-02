from celery import shared_task
from django.conf import settings


@shared_task
# def debug():
# 	print('DEBUG\n' * 10)
# 	from time import sleep
# 	sleep(10)
def send_mail(subject, message):
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )