from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explorer
        fields = ['first_name', 'last_name', 'street', 'city', 'state','username']
        # , 'restScore', 'entScore', 'savedEnt', 'savedRest', 'total_refresh', 'total_usage']