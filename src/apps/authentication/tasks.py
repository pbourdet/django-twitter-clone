from typing import NoReturn

from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_registration_email(first_name: str, email: str) -> NoReturn:
    send_mail(
        subject="Welcome to Twitter clone !",
        message=f"Hello {first_name} ! Thank you for your registration to Twitter clone.",
        from_email="contact@twitter-clone.com",
        recipient_list=[email],
    )
