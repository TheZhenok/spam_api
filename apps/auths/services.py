from django.core.mail import send_mail


def send(user_email: str):
    send_mail(
        'Подтверждение почты',
        'Пожалуйста, посмотрите наверх',
        'zhenok1109@gmail.com',
        [user_email],
        fail_silently=False
    )