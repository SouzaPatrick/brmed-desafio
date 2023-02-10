from rest_framework.response import Response
from rest_framework.views import APIView


class HighchartsAPIView(APIView):
    def get(self, request):
        return Response({"BRL": [5.24, 5.00, 5.67, 5.24, 5.00]})
