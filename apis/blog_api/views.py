from rest_framework import generics
from rest_framework import filters

from django.shortcuts import get_object_or_404


from .pagination import BasicPagination
from .serializers import (
                          
                          BlogPostDetialApiSerializer
                            )

from apis.posts_api.serializers import PostApiSerializer
from apis.vars import ALLOWED_POST_FIELDS

from ..models import PostApiModel,CommentApiModel
from ..comments_api.serializers import CommentApiSerializer


class PaginatedPostsListAPIView(generics.ListAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = PostApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    
    ordering_fields = ALLOWED_POST_FIELDS
    pagination_class = BasicPagination
        
    
class PaginatedPostsSearchAPIView(generics.ListAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = PostApiSerializer
    filter_backends =[filters.SearchFilter]
    
    search_fields = ['=id','title',
                     '=author_email',
                     'author_name',
                     ]
    
    pagination_class = BasicPagination


class PostsDetailAPIView(generics.RetrieveAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = BlogPostDetialApiSerializer


class AuthorPostsListAPIView(generics.ListAPIView):
    serializer_class = PostApiSerializer
    pagination_class = BasicPagination
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['id','title']

    def get_queryset(self):
        author_id = self.kwargs.get('pk')
        return PostApiModel.objects.filter(author_id=author_id)


class PostCommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = [
                       'id','user_id',
                       'username','email'
                       ]
                     
    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return CommentApiModel.objects.filter(post_id=post_id)
    

class PostCommentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = CommentApiSerializer
    
    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return CommentApiModel.objects.filter(post_id=post_id)
    
    def get_object(self):
        queryset = self.get_queryset()
        comment_id = self.kwargs.get('comment_id')
        obj = get_object_or_404(queryset, id=comment_id)
        self.check_object_permissions(self.request, obj)
        return obj
