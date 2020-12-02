from rest_framework import routers
from django.urls import path,include

from .views import (PostAPIViewSet,
                    PostsSearchAPIView,
                    PostsRandomAPIView)

router = routers.DefaultRouter()
router.register('',PostAPIViewSet,basename='posts_api')


urlpatterns = [
        path('search/',PostsSearchAPIView.as_view(),name='posts_search'),
        path('random/',PostsRandomAPIView.as_view(),name='posts_random'),
        path('',include(router.urls)),
        ]
