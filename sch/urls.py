from django.urls import path

from .views import SCH, CHECK, PWR, SCHDashboard

# from .views import SCH, CHECK

urlpatterns = [
    path("client/", SCH.as_view()),
    path("", CHECK.as_view()),
    path("power/", PWR.as_view()),
    path("client-dashboard/", SCHDashboard.as_view()),
]
