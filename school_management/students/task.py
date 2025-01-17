from celery import shared_task
from time import sleep

@shared_task
def send_welcome_email():
    sleep(5)  # Simulating sending an email
    return "Email sent"