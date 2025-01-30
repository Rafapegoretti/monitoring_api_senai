from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MonitoringDataSerializer
from .services import save_evidence_image
from .models import MonitoringData
from drf_spectacular.utils import extend_schema


class MonitoringView(APIView):
    @extend_schema(
        request=MonitoringDataSerializer, responses={201: {"message": "Msg_success"}}
    )
    def post(self, request):
        serializer = MonitoringDataSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            # Salvar a imagem de evidência
            evidence_path = save_evidence_image(
                validated_data["mac"],
                validated_data["date"],
                validated_data["evidence"],
            )

            # Criar o registro no banco de dados
            MonitoringData.objects.create(
                mac=validated_data["mac"],
                date=validated_data["date"],
                object_class=validated_data["object_class"],
                evidence_path=evidence_path,
            )

            return Response({"message": "Msg_success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
