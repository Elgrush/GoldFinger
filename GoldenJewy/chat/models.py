from django.db import models


class TelegramMessage(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    chat_id = models.BigIntegerField()

    def __str__(self):
        return self.name