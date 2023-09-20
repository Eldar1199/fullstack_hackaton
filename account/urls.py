from django.urls import path
from.views import RegisterRecruiterView, RegisterUserView, ActivationUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('rec-reg/', RegisterRecruiterView.as_view(), name='recruiter_register'),
    path('rec-act/<str:email>/<str:activation_code>', ActivationUserView.as_view(), name='recruiter_activation'),
    path('rec-log/', TokenObtainPairView.as_view(), name='recruiter_token_obtain_pair'),
    path('rec-ref/', TokenRefreshView.as_view(), name='recruiter_token_refresh'),


    path('user-reg/', RegisterUserView.as_view(), name='user_register'),
    path('user-act/<str:email>/<str:activation_code>', ActivationUserView.as_view(), name='user_activation'),
    path('user-log/', TokenObtainPairView.as_view(), name='user_token_obtain_pair'),
    path('user-ref/', TokenRefreshView.as_view(), name='user_token_refresh'),

]
