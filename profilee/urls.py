from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileUserView, ProfileReqruiterView


router = DefaultRouter()


router.register('profile', ProfileUserView)
router.register('profiles', ProfileReqruiterView)

urlpatterns = [
    path('', include(router.urls)),
]