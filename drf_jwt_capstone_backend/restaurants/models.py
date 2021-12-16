from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    review_rating = models.IntegerField()
    date_visited = models.IntegerField()
    location = models.IntegerField()
 