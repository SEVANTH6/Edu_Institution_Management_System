from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

#for handling all student operations
class AllStudentAPIView(APIView):
    def get(self, request):
        return Response({"message": "Student API Endpoint"})

    def post(self, request):
        return Response({"message": "Student API POST request"})

    

#for handling individual student operations
class OneStudentAPIView(APIView):
    def get(self, request, student_id):
        return Response({"message": f"Student API Endpoint for student {student_id}"})
    
    def put(self, request, student_id):
        return Response({"message": f"Student API PUT request for student {student_id}"})

    def delete(self, request, student_id):
        return Response({"message": f"Student API DELETE request for student {student_id}"})
    



#for handling all faculty operations
class AllFacultyAPIView(APIView):
    def get(self, request):
        return Response({"message": "Faculty API Endpoint"})

    def post(self, request):
        return Response({"message": "Faculty API POST request"})

#for handling individual faculty operations
class OneFacultyAPIView(APIView):
    def get(self, request, faculty_id):
        return Response({"message": f"Faculty API Endpoint for faculty {faculty_id}"})
    
    def put(self, request, faculty_id):
        return Response({"message": f"Faculty API PUT request for faculty {faculty_id}"})

    def delete(self, request, faculty_id):
        return Response({"message": f"Faculty API DELETE request for faculty {faculty_id}"})