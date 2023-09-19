from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileUserView, ProfileReqruiterView


router = DefaultRouter()


router.register('user', ProfileUserView)
router.register('req', ProfileReqruiterView)

urlpatterns = [
    path('', include(router.urls)),
]