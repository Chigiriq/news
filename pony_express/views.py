from .custom_factories import CustomEmailFactory
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from pony_express.models import OutgoingEmail
from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article

def send_newsletter(recipients):
    subject = "Your Monthly Newsletter"
    
    # Render the newsletter HTML content
    content = render_to_string('newsletter.html', {'content': 'Here is the latest content for you!'})

    # Create the email object
    email = EmailMessage(
        subject=subject,
        body=content,
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

    #console printing
    print("Email Subject:", email.subject)
    # print("Email Body:", email.body)  all html if uncommented
    print("Recipients:", email.to)

    #Save email
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

def send_newsletter_view(request):
    recipients = ['recipient1@example.com', 'recipient2@example.com']
    #above would be replaced with users with emails
    send_newsletter(recipients)
    return HttpResponse("Newsletter details printed to console!")


def newsletter_view(request):
    articles = Article.objects.all()
    context = {
        'content': 'Here is the latest content for you!',
        'article_list': articles
    }
    return render(request, 'newsletter.html', context)
