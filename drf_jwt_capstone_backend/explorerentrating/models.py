from django.db import models

from drf_jwt_capstone_backend.explorers.models import Explorer

# Create your models here.
class ExplorerEntRating(models.Model):
    rating = models.ForeignKey(Explorer, on_delete=models.CASCADE)
    