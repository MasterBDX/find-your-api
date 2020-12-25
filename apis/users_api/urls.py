from rest_framework.routers import DefaultRouter

from django.urls import path,include

from .views import UserAPIViewSet,UsersSearchAPIView,UsersRandomAPIView

app_name = 'users_api'

router = DefaultRouter()
router.register('', UserAPIViewSet, basename='api')

app_name = 'users_api'

urlpatterns = [
        path('search/',UsersSearchAPIView.as_view(),name='api-search'),
        path('random/',UsersRandomAPIView.as_view(),name='api-random'),
        path('', include(router.urls)),
        ]

