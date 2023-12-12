from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField(to="Language")


class Language(models.Model):
    name = models.CharField(max_length=100)
