from django.db import models

# from drf_jwt_capstone_backend.explorerentratings.models import ExplorerEntRating
# from drf_jwt_capstone_backend.explorerentertainments.models import ExplorerEntertainment
# from drf_jwt_capstone_backend.explorerentratings.models import ExplorerEntRating
# from drf_jwt_capstone_backend.explorerrestaurants.models import ExplorerRestaurant
# from drf_jwt_capstone_backend.explorerrestratings.models import ExplorerRestRating



class Explorer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    total_refresh = models.IntegerField()
    total_usage = models.IntegerField()
    # restScore = models.ForeignKey('explorerrestratings.ExplorerRestRating', on_delete=models.CASCADE)
    # entScore = models.ForeignKey('explorerentratings.ExplorerEntRating', on_delete=models.CASCADE)
    location = models.CharField(max_length=250)
    # savedEnt = models.ForeignKey('explorerentertainments.ExplorerEntertainment', blank=True, null=True,  on_delete=models.CASCADE)
    # savedRest = models.ForeignKey('explorerrestaurants.ExplorerRestaurant', blank=True, null=True,  on_delete=models.CASCADE)
   
    # def __str__(self):
    #    return self.firstName


# Create your models here.
