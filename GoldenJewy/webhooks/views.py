from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.tasks import send_telegram_reply

class TelegramWebhook(APIView):
    def post(self, request, token):
        if token != settings.TELEGRAM_WEBHOOK_TOKEN:
            return Response(
                {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
            )

        send_telegram_reply.delay(request.data)

        return Response({"success": True})