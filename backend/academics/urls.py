from django.urls import path
from . import views

urlpatterns = [
    # Branch URLs
    path("Branch/", views.AllBranchAPIView.as_view(), name="branch_api"),
    path("Branch/<int:branch_id>/", views.OneBranchAPIView.as_view(), name="one_branch_api"),

    # Batch URLs
    path("Batch/", views.AllBatchAPIView.as_view(), name="batch_api"),
    path("Batch/<int:batch_id>/", views.OneBatchAPIView.as_view(), name="one_batch_api"),

    # Subject URLs
    path("Subject/", views.AllSubjectAPIView.as_view(), name="subject_api"),
    path("Subject/<int:subject_id>/", views.OneSubjectAPIView.as_view(), name="one_subject_api"),

    # Class URLs
    path("Class/", views.AllClassAPIView.as_view(), name="class_api"),
    path("Class/<int:class_id>/", views.OneClassAPIView.as_view(), name="one_class_api"),

    # Class_Sub URLs
    path("ClassSub/", views.AllClassSubAPIView.as_view(), name="classsub_api"),
    path("ClassSub/<int:class_sub_id>/", views.OneClassSubAPIView.as_view(), name="one_classsub_api"),
]