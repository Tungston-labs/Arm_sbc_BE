from django.urls import path
from .views import AdminLoginView,ForgotPasswordView,VerifyOTPView,ResetPasswordView,ChangePasswordView,LogoutView,TokenRefreshCustomView

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin-login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("logout/", LogoutView.as_view(), name="logout"),
     path("token/refresh/", TokenRefreshCustomView.as_view(), name="token-refresh"),
]
