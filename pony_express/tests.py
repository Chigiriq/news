from django.test import TestCase
from .custom_factories import CustomEmailFactory
from pony_express.models import OutgoingEmail

class CustomEmailFactoryTest(TestCase):
    def test_email_creation(self):
        factory = CustomEmailFactory()
        email = factory.create_email(
            recipient="test@example.com",
            subject="Test Subject",
            message="This is a test message."
        )

        self.assertIsInstance(email, OutgoingEmail)
        self.assertEqual(email.to, "test@example.com")
        self.assertEqual(email.subject, "Test Subject")
        self.assertEqual(email.message, "This is a test message.")
