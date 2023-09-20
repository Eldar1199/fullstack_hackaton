from django.urls import path
from .views import ProfileUserAPIView, ProfileReqruiterAPIView


urlpatterns = [
    path('user/', ProfileUserAPIView.as_view()),
    path('req/', ProfileReqruiterAPIView.as_view()),
]