from django.db import models

# from drf_jwt_capstone_backend.explorers.models import Explorer
# from drf_jwt_capstone_backend.restaurants.models import Restaurant

# Create your models here.
class ExplorerRestaurant(models.Model):
    explorerId = models.ForeignKey('explorers.Explorer', blank=True, null=True,  on_delete=models.CASCADE)
    restaurantId = models.ForeignKey('restaurants.Restaurant', blank=True, null=True,  on_delete=models.CASCADE)
    
