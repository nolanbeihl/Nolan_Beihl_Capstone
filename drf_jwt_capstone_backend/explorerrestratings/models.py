from django.db import models
# from drf_jwt_capstone_backend.entertainments.models import Entertainment

# from drf_jwt_capstone_backend.explorers.models import Explorer

# Create your models here.
class ExplorerRestRating(models.Model):

   explorerId = models.ForeignKey('explorers.Explorer', blank=True, null=True,  on_delete=models.CASCADE)
   restaurantId = models.ForeignKey('restaurants.Restaurant', blank=True, null=True,  on_delete=models.CASCADE)
