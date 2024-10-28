from django.urls import path
from .views import send_newsletter_view

urlpatterns = [
    path('send-newsletter/', send_newsletter_view, name='send_newsletter'),
]
