from django.db import models

# Create your models here.
class UsefulLink(models.Model):
    link = models.URLField()
    description = models.TextField()