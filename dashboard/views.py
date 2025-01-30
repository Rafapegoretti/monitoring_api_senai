from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DashboardSerializer
from .services import get_filtered_occurrences


class DashboardView(APIView):
    def get(self, request, day=0, month=0, year=0):
        # Obter os dados filtrados
        occurrences = get_filtered_occurrences(day, month, year)

        # Serializar os dados
        serializer = DashboardSerializer(
            occurrences, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
