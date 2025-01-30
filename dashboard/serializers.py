from rest_framework import serializers
from monitoring.models import MonitoringData


class DashboardSerializer(serializers.ModelSerializer):
    evidence_url = serializers.SerializerMethodField()

    class Meta:
        model = MonitoringData
        fields = ["mac", "object_class", "date", "evidence_url"]

    def get_evidence_url(self, obj):
        # Gerar URL para a imagem com base na requisição
        request = self.context.get("request")
        if obj.evidence_path:
            return request.build_absolute_uri(f"/media/{obj.evidence_path}")
        return None
