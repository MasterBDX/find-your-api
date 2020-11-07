from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters

from django.utils.timesince import timesince
from django.conf import settings
from django.shortcuts import get_object_or_404

from .serializers import PostApiSerializer,PostAddApiSerializer

from .utils import *

from ..models import PostApiModel
from ..utils import check_ordering_kwarg,clean_pk

class PostAPIViewSet(viewsets.ViewSet):
    '''  Viewset to handle GET POST PUT PATCH DELETE requests for
            my Posts API 
             '''
    def list(self, request):
        try:
            limit = int(request.GET.get('limit',None))
        except:
            limit = None
        fields = ['id','title','published_at','author']
        ordering = check_ordering_kwarg(request.GET.get('ordering'),
                                        fields)               
               
        if ordering:
            queryset = PostApiModel.objects.order_by(ordering)
        else:
            queryset = PostApiModel.objects.all()
        serialized_data = PostApiSerializer(queryset[:limit],many=True)
        return Response(serialized_data.data)

    def create(self, request):
        last_user = PostApiModel.objects.values('id').last()
        obj_id = last_user.get('id') + 1
        serialized_data = PostAddApiSerializer(data=request.data)
        if serialized_data.is_valid():
            return Response({'id':obj_id,
                      **json_post_object(serialized_data.validated_data)})
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(PostApiModel,pk=pk)
        serilaizerd_obj = PostApiSerializer(instance=obj)
        return Response(serilaizerd_obj.data)

    def update(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(PostApiModel,pk=pk)
        serialized_data = PostAddApiSerializer(instance=obj,data=request.data)
        if serialized_data.is_valid():
        
            return Response({'id':obj.id,
                             **json_post_object(serialized_data.validated_data)
                             })
        return Response(serialized_data.errors,status=400)

    def partial_update(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(PostApiModel,pk=pk)
        serialized_data = PostAddApiSerializer(instance=obj,data=request.data)
        if serialized_data.is_valid():
            return Response({'id':obj.id,
                        **json_post_object(serialized_data.validated_data)
                    })
        return Response(serialized_data.errors,status=400)

    def destroy(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(PostApiModel,pk=pk)
        return Response("Post has been deleted")


class PostsSearchAPIView(ListAPIView):
    ''' View for search about users using search filter  '''

    queryset = PostApiModel.objects.all()
    serializer_class = PostApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['id','title','user_id','published_at']
    
    search_fields = ['id','title','overview','content',
                     'user_id__username','user_id__full_name']
    

class PostsRandomAPIView(ListAPIView):
    queryset = PostApiModel.objects.order_by('?')
    serializer_class = PostApiSerializer
    
    def get_queryset(self):
        try:
            limit = int(self.request.GET.get('limit','10'))
        except:
            limit = 10
        return self.queryset[:limit]
