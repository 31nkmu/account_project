from rest_framework.routers import DefaultRouter

from applications.spam import views

router = DefaultRouter()
router.register('', views.SpamViewSet)

urlpatterns = router.urls
