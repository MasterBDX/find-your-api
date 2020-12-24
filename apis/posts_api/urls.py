from rest_framework import routers
from django.urls import path,include

from .views import (PostAPIViewSet,
                    PostsSearchAPIView,
                    PostsRandomAPIView)

router = routers.DefaultRouter()
router.register('',PostAPIViewSet,basename='api')

app_name = 'posts_api'

urlpatterns = [
        path('search/',PostsSearchAPIView.as_view(),name='api-search'),
        path('random/',PostsRandomAPIView.as_view(),name='api-random'),
        path('',include(router.urls)),
        ]

