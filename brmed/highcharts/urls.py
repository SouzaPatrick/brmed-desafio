from django.urls import path

from .views import HighchartsView

urlpatterns = [
    path("", HighchartsView.as_view(), name="graph"),
]
