from django.urls import path
from .views import ProfileUserAPIView, ProfileRecruiterAPIView

urlpatterns = [
    path('user/', ProfileUserAPIView.as_view()),
    path('reс/', ProfileRecruiterAPIView.as_view()),
]