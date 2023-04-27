from django.urls import path
from .views import SCH,CHECK,PWR

urlpatterns = [
    path("", SCH.as_view()),
    path("check/", CHECK.as_view()),
    path("power/", PWR.as_view())
]
