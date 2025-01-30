from rest_framework import serializers


class MonitoringDataSerializer(serializers.Serializer):
    mac = serializers.CharField(max_length=50)
    date = serializers.DateTimeField()
    object_class = serializers.CharField(max_length=100)
    evidence = serializers.CharField(write_only=True)  # Base64 string da imagem
