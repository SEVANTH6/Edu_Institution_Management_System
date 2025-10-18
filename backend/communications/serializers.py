from rest_framework import serializers
from .models import *

class ParentAlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentAlerts
        fields = '__all__'