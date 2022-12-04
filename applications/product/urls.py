from django.urls import path

from applications.product import views

urlpatterns = [
    # path('list/', views.ProductListApiView.as_view()),
    # path('create/', views.ProductCreateApiView.as_view()),
    path('', views.ProductListCreateApiView.as_view()),
    # path('<int:pk>/', views.ProductDetailApiView.as_view()),
    path('<int:pk>/', views.ProductRetrieveUpdateDestroyApiView.as_view()),
]
