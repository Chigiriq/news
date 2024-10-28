from django.shortcuts import render
from .factories import CustomEmailFactory

def send_notification(request):
    factory = CustomEmailFactory()
    email = factory.create_email(
        recipient="user@example.com",
        subject="Welcome!",
        message="Thank you for signing up!"
    )
    # handle email sending logic here
