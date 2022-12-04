from django.core.mail import send_mail


def send_hello(email):
    send_mail(
        'Вас приветствует крутой сайт',
        'привет как дела?',
        'karimovbillal20002@gmail.com',
        [email]
    )


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'karimovbillal20002@gmail.com',
        [email]
    )
