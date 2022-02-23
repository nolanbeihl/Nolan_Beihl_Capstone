from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    # savedRest = models.CharField(max_length=100)
    # savedEnt = models.CharField(max_length=100)
    # restScore = models.IntegerField(max_length=10)
    # entScore = models.IntegerField(max_length=10)
    firstName= models.CharField(max_length=100)
    lastName= models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    # userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # total_refresh = models.IntegerField(max_length=100)
    # total_usage = models.IntegerField(max_length=100)
  
