from rest_framework import generics
from rest_framework import filters

from django.shortcuts import get_object_or_404

from ..models import PostApiModel

from .pagination import BasicPagination
from .serializers import (
                          BlogPostApiSerializer,
                          BlogPostDetialApiSerializer
                            )

from ..comments_api.serializers import CommentApiSerializer


class PaginatedPostsListAPIView(generics.ListAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = BlogPostApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    
    ordering_fields = ['id','title','author_id','published_at']
    
    search_fields = ['id','title','overview','content','author_id__email',
                     'author_id__username','author_id__full_name']
    
    pagination_class = BasicPagination
        

class PostsDetailAPIView(generics.RetrieveAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = BlogPostDetialApiSerializer


class AuthorPostsListAPIView(generics.ListAPIView):
    serializer_class = BlogPostApiSerializer
    def get_queryset(self):
        author_id = self.kwargs.get('pk')
        return PostApiModel.objects.filter(author_id__id=author_id)


class PostCommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = [
                       'id','post_id',
                       'created_at','user_id',
                       'username','email'
                       ]
                     
    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return get_object_or_404(PostApiModel,id=post_id).comments.all()
    

class PostCommentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentApiSerializer
    
    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return get_object_or_404(PostApiModel,id=post_id).comments.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        comment_id = self.kwargs.get('comment_id')
        obj = get_object_or_404(queryset, id=comment_id)
        self.check_object_permissions(self.request, obj)
        return obj