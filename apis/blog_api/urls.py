from django.urls import path



from .views import (PaginatedPostsListAPIView,
                    PostsDetailAPIView,
                    AuthorPostsListAPIView,
                    PostCommentsListAPIView,
                    PostCommentDetailAPIView)


urlpatterns = [
        path('', PaginatedPostsListAPIView.as_view(), name='paginated-list'),
        path('<int:pk>/', PostsDetailAPIView.as_view(), name='detail'),
        path('author/<int:pk>/posts/', AuthorPostsListAPIView.as_view(), name='author_posts'),
        path('<int:pk>/comments/', PostCommentsListAPIView.as_view(), name='post_comments'),
        path('<int:pk>/comments/<int:comment_id>/', PostCommentDetailAPIView.as_view(), name='post_comment_detail'),
        ]
