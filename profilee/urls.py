from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileUserView, ProfileRecruiterView


router = DefaultRouter()


router.register('user', ProfileUserView)
router.register('req', ProfileRecruiterView)

urlpatterns = [
    path('', include(router.urls)),
]