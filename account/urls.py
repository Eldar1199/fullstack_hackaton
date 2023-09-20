from django.urls import path
from.views import RegisterRecruiterView, ActivationRecruiterView, RegisterUserView, ActivationUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('rec-reg/', RegisterRecruiterView.as_view(), name='register'),
    path('rec-act/<str:email>/<str:activation_code>', ActivationRecruiterView.as_view(), name='activate'),
    path('rec-log/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('rec-ref/', TokenRefreshView.as_view(), name='token_refresh'),


    path('user-reg/', RegisterUserView.as_view(), name='register'),
    path('user-act/<str:email>/<str:activation_code>', ActivationUserView.as_view(), name='activate'),
    path('user-log/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user-ref/', TokenRefreshView.as_view(), name='token_refresh'),

]
