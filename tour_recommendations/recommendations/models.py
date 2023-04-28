from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    categories = models.ManyToManyField(to='Category')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


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
