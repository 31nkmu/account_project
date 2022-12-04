from django.urls import path

from applications.account import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('logout/', views.LogoutApiView.as_view()),
    path('change_password/', views.ChangePasswordApiView.as_view()),
    path('send_mail/', views.send_hello_api_view),
    path('activate/<uuid:activation_code>/', views.ActivationApiView.as_view()),
]
