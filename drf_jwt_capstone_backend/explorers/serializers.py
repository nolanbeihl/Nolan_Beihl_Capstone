from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explorer
        fields = ['firstName', 'lastName', 'location', 'total_refresh', 'total_usage',]