from rest_framework import viewsets,generics
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.authentication import  BasicAuthentication 

from django.shortcuts import get_object_or_404

from .utils import get_new_comment,get_serialized_data
from .serializers import CommentApiSerializer,CommentAddApiSerializer

from ..authentication import CsrfExemptSessionAuthentication
from ..models import CommentApiModel
from ..global_utils import (check_ordering_kwarg,
                            clean_pk,
                            get_limit)

from random import randint

class CommentAPIViewSet(viewsets.ViewSet):
    '''  
         Viewset to handle GET POST PUT PATCH DELETE 
         requests for my Comments API 
    '''
    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)

    def list(self, request):
        limit = get_limit(request.GET)
        fields = ['id','post_id','user_id']
        order_attr = request.GET.get('ordering') 
        ordering = check_ordering_kwarg(order_attr,fields)               
               
        if ordering:
            queryset = CommentApiModel.objects.select_related('user_id').order_by(ordering)
        else:
            queryset = CommentApiModel.objects.select_related('user_id')
        serialized_data = CommentApiSerializer(queryset[:limit],many=True)
        return Response(serialized_data.data)

    def create(self, request):
        last_comment = CommentApiModel.objects.values('id').last()
        serialized_data = CommentAddApiSerializer(data=request.data)
        if serialized_data.is_valid():
            return Response(get_new_comment(serialized_data.validated_data,
                                            last_id=last_comment.get('id')))
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        data,status_ = get_serialized_data(pk=pk)
        return Response(data,status_)

    def update(self, request, pk=None):
        data,status_ = get_serialized_data(pk=pk,data=request.data)
        return Response(data,status_)

    def partial_update(self, request, pk=None):
        data,status_ = get_serialized_data(pk=pk,data=request.data,partial=True)
        return Response(data,status_)

    def destroy(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(CommentApiModel,pk=pk)
        return Response("Comment has been deleted")


class CommentsSearchAPIView(ListAPIView):
    ''' View for search about comments using search filter  '''

    queryset = CommentApiModel.objects.select_related('user_id')
    serializer_class = CommentApiSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['=id','=user_id__email','=post_id','=created_at',
                     'content','user_id__full_name',
                     'user_id__username',
                     ]

    

class CommentsRandomAPIView(ListAPIView):
    ''' 
        View to get random comments 
        by default get 10 but user can 
        select a custom limit
    '''

    queryset = CommentApiModel.objects.select_related('user_id').order_by('?')
    serializer_class = CommentApiSerializer
    
    def get_queryset(self):
        limit = get_limit(self.request.GET,initial=50)
        return self.queryset[:limit]
