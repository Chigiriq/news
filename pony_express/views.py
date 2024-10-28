from .custom_factories import CustomEmailFactory
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from pony_express.models import OutgoingEmail
from django.http import HttpResponse

# pony_express/views.py

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from pony_express.models import OutgoingEmail  # Adjust based on your structure

def send_newsletter(recipients):
    subject = "Your Monthly Newsletter"
    
    # Render the newsletter HTML content
    content = render_to_string('newsletter.html', {'content': 'Here is the latest content for you!'})

    # Create the email object
    email = EmailMessage(
        subject=subject,
        body=content,  # This should already be the rendered HTML
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipients,
    )

    # Specify that the email body is HTML
    email.content_subtype = 'html'

    # Send the email
    try:
        email.send()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

    # Print the email details to the console for debugging
    print("Email Subject:", email.subject)
    # print("Email Body:", email.body)  #all html
    print("Recipients:", email.to)

    # Save the email record (if needed)
    outgoing_email = OutgoingEmail(
        to=", ".join(recipients),
        subject=subject,
        message=content
    )
    outgoing_email.save()


def send_notification(request):
    factory = CustomEmailFactory()
    email = factory.create_email(
        recipient="user@example.com",
        subject="Welcome!",
        message="Thank you for signing up!"
    )


# handle email sending logic here
def send_newsletter_view(request):
    recipients = ['recipient1@example.com', 'recipient2@example.com']  # Replace with actual recipient list
    send_newsletter(recipients)
    return HttpResponse("Newsletter details printed to console!")

