from django.urls import path
from .views import DashboardView

urlpatterns = [
    path(
        "<int:day>/<int:month>/<int:year>/", DashboardView.as_view(), name="dashboard"
    ),
]
