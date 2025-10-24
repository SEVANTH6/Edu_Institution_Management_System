from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


# --Fees Record View--
#for handling all fees record operations
class AllFeesRecordAPIView(APIView):
    def get(self, request):
        return Response({"message": "Fees Record API Endpoint"})

    def post(self, request):
        return Response({"message": "Fees Record API POST request"})
    
#for handling individual fees record operations
class OneFeesRecordAPIView(APIView):
    def get(self, request, fee_id):
        return Response({"message": f"Fees Record API Endpoint for record {fee_id}"})

    def put(self, request, fee_id):
        return Response({"message": f"Fees Record API PUT request for record {fee_id}"})

    def delete(self, request, fee_id):
        return Response({"message": f"Fees Record API DELETE request for record {fee_id}"})
    

# --Marks View--
#for handling all marks operations
class AllMarksAPIView(APIView):
    def get(self, request):
        return Response({"message": "Marks API Endpoint"})

    def post(self, request):
        return Response({"message": "Marks API POST request"})

#for handling individual marks operations
class OneMarksAPIView(APIView):
    def get(self, request, marks_id):
        return Response({"message": f"Marks API Endpoint for marks {marks_id}"})

    def put(self, request, marks_id):
        return Response({"message": f"Marks API PUT request for marks {marks_id}"})

    def delete(self, request, marks_id):
        return Response({"message": f"Marks API DELETE request for marks {marks_id}"})


# --Backlogs View--
#for handling all backlogs operations
class AllBacklogsAPIView(APIView):
    def get(self, request):
        return Response({"message": "Backlogs API Endpoint"})

    def post(self, request):
        return Response({"message": "Backlogs API POST request"})

#for handling individual backlogs operations
class OneBacklogsAPIView(APIView):
    def get(self, request, backlog_id):
        return Response({"message": f"Backlogs API Endpoint for backlog {backlog_id}"})

    def put(self, request, backlog_id):
        return Response({"message": f"Backlogs API PUT request for backlog {backlog_id}"})

    def delete(self, request, backlog_id):
        return Response({"message": f"Backlogs API DELETE request for backlog {backlog_id}"})
    

# --Attendance View--
#for handling all attendance operations
class AllAttendanceAPIView(APIView):
    def get(self, request):
        return Response({"message": "Attendance API Endpoint"})

    def post(self, request):
        return Response({"message": "Attendance API POST request"})

#for handling individual attendance operations
class OneAttendanceAPIView(APIView):
    def get(self, request, attendance_id):
        return Response({"message": f"Attendance API Endpoint for attendance {attendance_id}"})

    def put(self, request, attendance_id):
        return Response({"message": f"Attendance API PUT request for attendance {attendance_id}"})

    def delete(self, request, attendance_id):
        return Response({"message": f"Attendance API DELETE request for attendance {attendance_id}"})   