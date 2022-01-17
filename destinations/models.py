from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Region(models.Model):
    name = CharField(max_length = 50)
    introduction = models.TextField()

class Country(models.Model):
    name = CharField(max_length = 255)
    region = models.ForeignKey(Region, on_delete = models.CASCADE)

class Destination(models.Model):
    name = CharField(max_length = 255)
    country = ForeignKey(Country, on_delete = models.CASCADE)
    introduction = models.TextField()
    photo = models.ImageField(upload_to='static/img/')
    publisher = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'publisher')
