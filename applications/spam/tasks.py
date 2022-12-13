from django.core.mail import send_mail

from applications.spam.models import Spam
from config.celery import app

email_list = [queryset.email for queryset in Spam.objects.all()]


@app.task
def spam_message():
    send_mail(
        'привет, мы из py24',
        'как дела?',
        'karimovbillal20002@gmail.com',
        email_list
    )
