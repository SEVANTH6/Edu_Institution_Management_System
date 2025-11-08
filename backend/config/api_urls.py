from django.urls import path, include

urlpatterns = [
#     path("", include("academics.urls")),
    path("", include("accounts.urls")),
#     path("", include("communications.urls")),
    path("", include("records.urls")),
]