from django.core.mail import send_mail


def send_hello(email):
    send_mail(
        'Вас приветствует крутой сайт',
        'привет как дела?',
        'karimovbillal20002@gmail.com',
        [email]
    )
