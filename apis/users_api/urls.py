from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import UserAPIViewSet,UsersSearchAPIView,UsersRandomAPIView

app_name = 'users_api'

router = DefaultRouter()
router.register('', UserAPIViewSet, basename='users')

urlpatterns = list(router.urls)

urlpatterns += [
        path('search/',UsersSearchAPIView.as_view(),name='users_search'),
        path('random/',UsersRandomAPIView.as_view(),name='users_random'),

        ]
