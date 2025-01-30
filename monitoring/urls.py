from django.urls import path
from .views import MonitoringEventView

urlpatterns = [
    path("", MonitoringEventView.as_view(), name="monitoring"),
]
