from django.db import models



class Explorer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    # restScore = models.ForeignKey(ExplorerRestRating, on_delete=models.CASCADE)
    # entScore = models.ForeignKey(ExplorerEntRating, on_delete=models.CASCADE)
    location = models.IntegerField()
    # savedEnt = models.ForeignKey(ExplorerRestaurant, on_delete=models.CASCADE)
    # savedRest = models.ForeignKey(ExplorerEntertainment, on_delete=models.CASCADE)
   


# Create your models here.
