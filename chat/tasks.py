import requests
import json
from django.conf import settings


def send_telegram_reply(message):
    name = message["message"]["from"]["first_name"]
    text = message["message"]["text"]
    chat_id = message["message"]["chat"]["id"]


    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": 'Зайти в приложение',
                    "web_app": {'url': f"{settings.HOST_URL}/webapp/"}
                }
            ]
        ]
    }

    reply = f"Hi {name}! Got your message: {text}. "

    reply_url = f"https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/sendMessage"

    data = {"chat_id": chat_id, "text": reply, "reply_markup": json.dumps(keyboard)}

    print('\n', data['reply_markup'], '\n')

    requests.post(reply_url, data=data)
