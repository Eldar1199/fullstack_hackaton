from django.urls import path
from.views import RegisterUserView, ActivationUserView, ActivationRecruiterView, ChangePasswordView, ForgotPasswordView, ForgotPasswordCompleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='registration'),
    path('rec-act/<str:email>/<str:activation_code>', ActivationRecruiterView.as_view(), name='user_activation'),
    path('user-act/<str:email>/<str:activation_code>', ActivationUserView.as_view(), name='user_activation'),
    path('log/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('ref/', TokenRefreshView.as_view(), name='token_refresh'),

    path('change-pass/', ChangePasswordView.as_view()),
    path('forgot-pass/', ForgotPasswordView.as_view()),
    path('forgot-pass-compl/', ForgotPasswordCompleteView.as_view()),

]
'=============================================  последняя фиксация ============================================='