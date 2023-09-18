from django.urls import path
from.views import RegisterView, ActivationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('recruter-register/', RegisterView.as_view()),
    path('recruter-activate/<str:email>/<str:activation_code>', ActivationView.as_view(), name='activate'),
    path('recruter-login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('recruter-refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

        