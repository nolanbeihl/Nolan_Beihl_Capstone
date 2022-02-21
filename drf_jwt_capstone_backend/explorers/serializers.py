from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explorer
        fields = ['firstName', 'lastName', 'street', 'city', 'state','userName']
        # , 'restScore', 'entScore', 'savedEnt', 'savedRest', 'total_refresh', 'total_usage']