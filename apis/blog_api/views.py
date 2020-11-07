from rest_framework import generics
from rest_framework import filters

from ..models import PostApiModel

from .pagination import BasicPagination
from .serializers import (
                          BlogPostApiSerializer,
                          BlogPostDetialApiSerializer
                            )


class PaginatedPostsListAPIView(generics.ListAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = BlogPostApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    
    ordering_fields = ['id','title','user_id','published_at']
    
    search_fields = ['id','title','overview','content','user_id__email',
                     'user_id__username','user_id__full_name']
    
    pagination_class = BasicPagination
    


                      
class PostsListAPIView(generics.ListAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = BlogPostApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    
    ordering_fields = ['id','title','user_id','published_at']
    
    search_fields = ['id','title','overview','content',
                     'user_id__username','user_id__full_name']
    

class PostsDetailAPIView(generics.RetrieveAPIView):
    queryset = PostApiModel.objects.all()
    serializer_class = BlogPostDetialApiSerializer



class AuthorPostsListAPIView(generics.ListAPIView):
    serializer_class = BlogPostApiSerializer

    def get_queryset(self):
        author_id = self.kwargs.get('pk')
        return PostApiModel.objects.filter(user_id__id=author_id)