# pony_express/models.py
from django.db import models

class OutgoingEmail(models.Model):
    to = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def send(self):
        # Implement the sending logic here
        pass
