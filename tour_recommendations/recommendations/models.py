from django.db import models
from django.conf import settings


class Events(models.Model):
    title = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    date = models.DateTimeField()
    end_reg = models.DateTimeField()
    categories = models.ManyToManyField(to='Category')
    description = models.TextField()
    image = models.ImageField()


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ChatHistory(models.Model):
    text = models.TextField()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(choices=('ai', 'user'))
    sent = models.DateTimeField()


