from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class StudentAPIView(APIView):
    def get(self, request):
        return Response({"message": "Student API Endpoint"})

    def post(self, request):
        return Response({"message": "Student API POST request"})

    def put(self, request):
        return Response({"message": "Student API PUT request"})

    def delete(self, request):
        return Response({"message": "Student API DELETE request"})