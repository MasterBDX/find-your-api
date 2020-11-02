from rest_framework import routers

from .views import PostAPIViewSet

router = routers.DefaultRouter()
router.register('',PostAPIViewSet,basename='posts_api')


urlpatterns = list(router.urls)
