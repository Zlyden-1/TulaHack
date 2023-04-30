from django.db import models
from django.conf import settings

from recommendations.models import Category, Events


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=Category, null=True, blank=True, through='UserPreferences')
    events = models.ManyToManyField(to=Events, through='EventRegister')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


class UserPreferences(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    interest_coef = models.FloatField(default=0.5)


class EventRegister(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    rated = models.BooleanField(default=False)
