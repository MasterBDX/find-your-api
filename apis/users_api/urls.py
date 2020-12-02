from rest_framework.routers import DefaultRouter

from django.urls import path,include

from .views import UserAPIViewSet,UsersSearchAPIView,UsersRandomAPIView

app_name = 'users_api'

router = DefaultRouter()
router.register('', UserAPIViewSet, basename='users')


urlpatterns = [
        path('', include(router.urls)),
        path('search/',UsersSearchAPIView.as_view(),name='users_search'),
        path('random/',UsersRandomAPIView.as_view(),name='users_random'),
        ]

