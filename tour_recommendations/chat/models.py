from django.db import models


class ChatHistory(models.Model):
    text = models.TextField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(choices=('ai', 'user'))
    sent = models.DateTimeField()

