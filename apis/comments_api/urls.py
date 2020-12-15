from rest_framework import routers
from django.urls import path,include

from .views import (CommentAPIViewSet,
                    CommentsSearchAPIView,
                    CommentsRandomAPIView)

router = routers.DefaultRouter()
router.register('',CommentAPIViewSet,basename='comments_api')


urlpatterns = [
        path('search/',CommentsSearchAPIView.as_view(),name='comments_search'),
        path('random/',CommentsRandomAPIView.as_view(),name='comments_random'),
        path('',include(router.urls)),
        ]
