from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    saved_rest = models.CharField(max_length=100)
    saved_ent = models.CharField(max_length=100)
    rest_score = models.IntegerField(max_length=10)
    ent_score = models.IntegerField(max_length=10)
    location = models.CharField(max_length=100)
    total_refresh = models.IntegerField(max_length=100)
    total_usage = models.IntegerField(max_length=100)
    
    def save_ent():
        
