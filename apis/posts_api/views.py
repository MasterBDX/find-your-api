from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.authentication import  BasicAuthentication 

from django.utils.timesince import timesince
from django.conf import settings
from django.shortcuts import get_object_or_404

from .serializers import PostApiSerializer,PostAddApiSerializer

from .utils import get_new_post,get_serialized_data

from ..authentication import CsrfExemptSessionAuthentication
from ..models import PostApiModel
from ..global_utils import (
                     check_ordering_kwarg,
                     clean_pk,
                     get_limit)


ALLOWED_ORDERING_FIELDS = ['id','title','author_id','author_name']

class PostAPIViewSet(viewsets.ViewSet):
    '''  Viewset to handle GET POST PUT PATCH DELETE requests for
            my Posts API 
             '''
    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)

    def list(self, request):
        limit = get_limit(request.GET)
        
        ordering = check_ordering_kwarg(request.GET.get('ordering'),
                                        ALLOWED_ORDERING_FIELDS)                              
        if ordering:
            queryset = PostApiModel.objects.order_by(ordering)
        else:
            queryset = PostApiModel.objects.all()
        serialized_data = PostApiSerializer(queryset[:limit],many=True)
        return Response(serialized_data.data)

    def create(self, request):
        serialized_data = PostAddApiSerializer(data=request.data)
        if serialized_data.is_valid():
            data = PostApiSerializer(instance=get_new_post(serialized_data.validated_data )).data
            return Response(data)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        data,status_ = get_serialized_data(clean_pk(pk))
        return Response(data,status=status_)
    
    def update(self, request, pk=None):
       data,status_ = get_serialized_data(clean_pk(pk),request.data)
       return Response(data,status_)

    def partial_update(self, request, pk=None):
        data,status_ = get_serialized_data(clean_pk(pk),request.data,partial=True)
        return Response(data,status_)
                   
    def destroy(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(PostApiModel,pk=pk)
        return Response("Post has been deleted")


class PostsSearchAPIView(ListAPIView):
    ''' View for search about users using search filter  '''

    queryset = PostApiModel.objects.all()
    serializer_class = PostApiSerializer
    filter_backends =[filters.SearchFilter]
    
    search_fields = ['=id','title',
                     '=author_email',
                     'author_name',
                     ]
    

class PostsRandomAPIView(ListAPIView):
    queryset = PostApiModel.objects.order_by('?')
    serializer_class = PostApiSerializer
    
    def get_queryset(self):
        limit = get_limit(self.request.GET,initial=20)
        return self.queryset[:limit]
