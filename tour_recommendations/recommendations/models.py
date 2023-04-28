from django.db import models

# Create your models here.

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
