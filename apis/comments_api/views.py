from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters

from django.shortcuts import get_object_or_404


from .utils import *
from .serializers import CommentApiSerializer,CommentAddApiSerializer
from ..models import CommentApiModel
from ..global_utils import check_ordering_kwarg,clean_pk



class CommentAPIViewSet(viewsets.ViewSet):
    '''  
         Viewset to handle GET POST PUT PATCH DELETE 
         requests for my Comments API 
    '''
    def list(self, request):
        try:
            limit = int(request.GET.get('limit',None))
        except:
            limit = None
        fields = ['id','post_id','user_id']
        ordering = check_ordering_kwarg(request.GET.get('ordering'),
                                        fields)               
               
        if ordering:
            queryset = CommentApiModel.objects.order_by(ordering)
        else:
            queryset = CommentApiModel.objects.all()
        serialized_data = CommentApiSerializer(queryset[:limit],many=True)
        return Response(serialized_data.data)

    def create(self, request):
        last_comment = CommentApiModel.objects.values('id').last()
        obj_id = randint(last_comment.get('id') + 1,100000)      
        serialized_data = CommentAddApiSerializer(data=request.data)
        if serialized_data.is_valid():
            return Response({'id':obj_id,
                             **json_comment_object(serialized_data.data)
                             })
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(CommentApiModel,pk=pk)
        serilaizerd_obj = CommentApiSerializer(instance=obj)
        return Response(serilaizerd_obj.data)

    def update(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(CommentApiModel,pk=pk)
        serilaizerd_data = CommentAddApiSerializer(instance=obj,data=request.data)
        if serilaizerd_data.is_valid():
            return Response({'id':obj.id,
                            **json_comment_object(serilaizerd_data.validated_data,created_at=obj.created_at)
                             })
        return Response(serilaizerd_data.errors,status=400)


    def partial_update(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(CommentApiModel,pk=pk)
        serilaizerd_data = CommentAddApiSerializer(instance=obj,data=request.data)
        if serilaizerd_data.is_valid():
            return Response({'id':obj.id,
                             **json_comment_object(serilaizerd_data.validated_data,created_at=obj.created_at)
            })
                             
        return Response(serilaizerd_data.errors,status=400)

    def destroy(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(CommentApiModel,pk=pk)
        return Response("Comment has been deleted")


class CommentsSearchAPIView(ListAPIView):
    ''' View for search about comments using search filter  '''

    queryset = CommentApiModel.objects.all()
    serializer_class = CommentApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = [
                       'id','post_id__title',
                       'created_at','user_id__username',
                       'user_id__full_name',
                       ]
    search_fields = ['id','post_id__title',
                     'content','created_at',
                     'user_id__full_name',
                     'user_id__username',
                     'user_id__email']

    

class CommentsRandomAPIView(ListAPIView):
    ''' 
        View to get random comments 
        by default get 10 but user can 
        select a custom limit
    '''

    queryset = CommentApiModel.objects.order_by('?')
    serializer_class = CommentApiSerializer
    
    def get_queryset(self):
        try:
            limit = int(self.request.GET.get('limit','10'))
        except:
            limit = 10
        return self.queryset[:limit]
