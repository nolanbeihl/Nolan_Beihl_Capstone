from django.db import models
# from drf_jwt_capstone_backend.entertainments.models import Entertainment
# from drf_jwt_capstone_backend.explorers.models import Explorer


# Create your models here.
class ExplorerEntertainment(models.Model):

   explorerId = models.ForeignKey('explorers.Explorer', blank=True, null=True, on_delete=models.CASCADE)
   entertainmentId = models.ForeignKey('entertainments.Entertainment', blank=True, null=True, on_delete=models.CASCADE)
