from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchesView, BatchesView, SubjectsView, ClassesView, Class_subView

router = DefaultRouter()
router.register(r'branches', BranchesView)
router.register(r'batches', BatchesView)
router.register(r'subjects', SubjectsView)
router.register(r'classes', ClassesView)
router.register(r'class-subjects', Class_subView)

urlpatterns = [
    path('', include(router.urls)),
]