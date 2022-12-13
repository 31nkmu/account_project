from django.core.mail import send_mail
from config.celery import app


@app.task
def send_confirmation_email_celery(email, code):
    import time
    # time.sleep(20)
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'karimovbillal20002@gmail.com',
        [email]
    )


# @app.task
# def spam_message():
#     send_mail(
#         'привет, мы из py24',
#         'как дела?',
#         'karimovbillal20002@gmail.com',
#         ['karimovbillal20002@gmail.com'],
#     )
