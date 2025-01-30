from rest_framework import serializers
from .models import MonitoringEvent


class MonitoringEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringEvent
        fields = ["mac", "date", "object_class", "evidence"]
