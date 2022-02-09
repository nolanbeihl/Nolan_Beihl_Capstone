from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explorer
        fields = ['firstName', 'lastName', 'street', 'city', 'state', 'total_refresh', 'total_usage', 'restScore', 'entScore', 'savedEnt', 'savedRest']