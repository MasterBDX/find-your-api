from rest_framework import routers
from django.urls import path,include

from .views import (CommentAPIViewSet,
                    CommentsSearchAPIView,
                    CommentsRandomAPIView,
                    CommnetsListAPIView)

router = routers.DefaultRouter()
router.register('',CommentAPIViewSet,basename='comments_api')


urlpatterns = [
        path('search/',CommentsSearchAPIView.as_view(),name='comments_search'),
        path('random/',CommentsRandomAPIView.as_view(),name='comments_random'),
        path('list/',CommnetsListAPIView.as_view(),name='comments_list'),
        path('',include(router.urls)),
        ]
