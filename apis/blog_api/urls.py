from django.urls import path



from .views import (PostsListAPIView,
                    PaginatedPostsListAPIView,
                    PostsDetailAPIView,
                    AuthorPostsListAPIView)


urlpatterns = [
        path('', PostsListAPIView.as_view(), name='list'),
        path('paginated/', PaginatedPostsListAPIView.as_view(), name='paginated-list'),
        path('<int:pk>/', PostsDetailAPIView.as_view(), name='detail'),
        path('author/<int:pk>/posts/', AuthorPostsListAPIView.as_view(), name='author_posts'),
        ]
