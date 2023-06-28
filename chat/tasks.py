import requests
from django.db import models
from django.conf import settings
from dispatcher.models import UserProfile


def send_telegram_reply(message):
    name = message["message"]["from"]["first_name"]
    text = message["message"]["text"]
    chat_id = message["message"]["chat"]["id"]

    '''
    try:
        print(UserProfile.objects.get(id=message["message"]["from"]["id"]))
    except UserProfile.DoesNotExist:
        pass
    '''

    reply = f"Hi {name}! Got your message: {text}. "

    reply_url = f"https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/sendMessage"

    data = {"chat_id": chat_id, "text": reply}

    requests.post(reply_url, data=data)
