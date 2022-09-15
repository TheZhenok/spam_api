from settings.celery import app
from auths.services import send


@app.task
def send_spam_email(user_email: str):
    send(user_email)