from django.db import models

# Create your models here.
class Player(models.model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    gsis_id = models.CharField(max_length=20)