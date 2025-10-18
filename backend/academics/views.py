from rest_framework.response import Response
from rest_framework.views import APIView

#--Branche View--
#for handling all branch operations
class AllBranchAPIView(APIView):
    def get(self, request):
        return Response({"message": "Branch API Endpoint"})

    def post(self, request):
        return Response({"message": "Branch API POST request"})


#for handling individual branch operations
class OneBranchAPIView(APIView):
    def get(self, request, branch_id):
        return Response({"message": f"Branch API Endpoint for branch {branch_id}"})

    def put(self, request, branch_id):
        return Response({"message": f"Branch API PUT request for branch {branch_id}"})

    def delete(self, request, branch_id):
        return Response({"message": f"Branch API DELETE request for branch {branch_id}"})
    


# --Batch View--
#for handling all batch operations
class AllBatchAPIView(APIView):
    def get(self, request):
        return Response({"message": "Batch API Endpoint"})
    
    def post(self, request):
        return Response({"message": "Batch API POST request"})

#for handling individual batch operations
class OneBatchAPIView(APIView):
    def get(self, request, batch_id):
        return Response({"message": f"Batch API Endpoint for batch {batch_id}"})
    
    def put(self, request, batch_id):
        return Response({"message": f"Batch API PUT request for batch {batch_id}"})

    def delete(self, request, batch_id):
        return Response({"message": f"Batch API DELETE request for batch {batch_id}"})


#--Subject View--
#for handling all subject operations
class AllSubjectAPIView(APIView):
    def get(self, request):
        return Response({"message": "Subject API Endpoint"})

    def post(self, request):
        return Response({"message": "Subject API POST request"})

#for handling individual subject operations
class OneSubjectAPIView(APIView):
    def get(self, request, subject_id):
        return Response({"message": f"Subject API Endpoint for subject {subject_id}"})

    def put(self, request, subject_id):
        return Response({"message": f"Subject API PUT request for subject {subject_id}"})

    def delete(self, request, subject_id):
        return Response({"message": f"Subject API DELETE request for subject {subject_id}"})




#--Class View--
#for handling all class operations
class AllClassAPIView(APIView):
    def get(self, request):
        return Response({"message": "Class API Endpoint"})

    def post(self, request):
        return Response({"message": "Class API POST request"})

#for handling individual class operations
class OneClassAPIView(APIView):
    def get(self, request, class_id):
        return Response({"message": f"Class API Endpoint for class {class_id}"})

    def put(self, request, class_id):
        return Response({"message": f"Class API PUT request for class {class_id}"})

    def delete(self, request, class_id):
        return Response({"message": f"Class API DELETE request for class {class_id}"})



#--ClassSub View--
#for handling all classsub operations
class AllClassSubAPIView(APIView):
    def get(self, request):
        return Response({"message": "ClassSub API Endpoint"})

    def post(self, request):
        return Response({"message": "ClassSub API POST request"})

#for handling individual classsub operations
class OneClassSubAPIView(APIView):
    def get(self, request, class_sub_id):
        return Response({"message": f"ClassSub API Endpoint for classSub {class_sub_id}"})

    def put(self, request, class_sub_id):
        return Response({"message": f"ClassSub API PUT request for classSub {class_sub_id}"})

    def delete(self, request, class_sub_id):
        return Response({"message": f"ClassSub API DELETE request for classSub {class_sub_id}"})