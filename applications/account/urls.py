from django.urls import path

from applications.account import views
from applications.account.views import send_hello_api_view

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('logout/', views.LogoutApiView.as_view()),
    path('change_password/', views.ChangePasswordApiView.as_view()),
    path('send_mail/', send_hello_api_view),
]
