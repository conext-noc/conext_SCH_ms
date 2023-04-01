from django.urls import path
from .views import SCH

urlpatterns = [
    path("", SCH.as_view()),
    path("<int:id>/", SCH.as_view(), name='contract')

]
