from django.urls import path
from .views import send_newsletter_view, newsletter_view

urlpatterns = [
    path('newsletter/', newsletter_view, name='newsletter'),
    path('send-newsletter/', send_newsletter_view, name='send_newsletter'),
]
