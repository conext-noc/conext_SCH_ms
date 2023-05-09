from django.urls import path
from .views import SCH,CHECK,PWR

urlpatterns = [
    path("client/", SCH.as_view()),
    path("", CHECK.as_view()),
    path("power/", PWR.as_view())
]
