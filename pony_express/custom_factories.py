# custom_factories.py in pony_express app
from pony_express.models import OutgoingEmail

class CustomEmailFactory:
    def create_email(self, recipient, subject, message):
        email = OutgoingEmail(
            to=recipient,
            subject=subject,
            message=message,
        )
        email.save()
        return email
