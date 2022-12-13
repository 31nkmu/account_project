from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    # path('login/', views.LoginApiView.as_view()),
    # path('logout/', views.LogoutApiView.as_view()),
    path('change_password/', views.ChangePasswordApiView.as_view()),
    path('send_mail/', views.send_hello_api_view),
    path('activate/<uuid:activation_code>/', views.ActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot_password/', views.ForgotPasswordApiView.as_view()),
    path('forgot_password_complete/', views.ForgotPasswordCompleteApiView.as_view()),
]
