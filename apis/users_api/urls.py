from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import UserAPIViewSet,UsersSearchAPIView,UsersRandomAPIView

app_name = 'users_api'

router = DefaultRouter()
router.register('', UserAPIViewSet, basename='users')

urlpatterns = list(router.urls)

urlpatterns += [
        path('search/users/',UsersSearchAPIView.as_view(),name='users_search'),
        path('random/users/',UsersRandomAPIView.as_view(),name='users_random'),

        ]
