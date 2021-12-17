from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explorer
        fields = ['firstName', 'lastName', 'restScore', 'entScore', 'location', 'savedEnt', 'savedRest']