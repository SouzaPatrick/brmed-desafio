from django.urls import path

from .views import HighchartsAPIView

urlpatterns = [
    path("", HighchartsAPIView.as_view(), name="graph-api"),
]
