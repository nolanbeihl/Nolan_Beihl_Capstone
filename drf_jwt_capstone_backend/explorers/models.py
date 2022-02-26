from django.db import models

# from drf_jwt_capstone_backend.explorerentratings.models import ExplorerEntRating
# from drf_jwt_capstone_backend.explorerentertainments.models import ExplorerEntertainment
# from drf_jwt_capstone_backend.explorerentratings.models import ExplorerEntRating
# from drf_jwt_capstone_backend.explorerrestaurants.models import ExplorerRestaurant
# from drf_jwt_capstone_backend.explorerrestratings.models import ExplorerRestRating



class Explorer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=4, blank=True, null=True)
    # total_refresh = models.IntegerField(blank=True, null=True)
    # total_usage = models.IntegerField(blank=True, null=True)
    # restScore = models.ForeignKey('explorerrestratings.ExplorerRestRating',blank=True, null=True, on_delete=models.CASCADE)
    # entScore = models.ForeignKey('explorerentratings.ExplorerEntRating', blank=True, null=True, on_delete=models.CASCADE)
    # savedEnt = models.ForeignKey('explorerentertainments.ExplorerEntertainment', blank=True, null=True,  on_delete=models.CASCADE)
    # savedRest = models.ForeignKey('explorerrestaurants.ExplorerRestaurant', blank=True, null=True,  on_delete=models.CASCADE)
   
    # def __str__(self):
    #    return self.firstName


# Create your models here.
