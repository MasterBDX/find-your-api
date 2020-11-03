from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import filters

from django.shortcuts import get_object_or_404

from .serializers import PostApiSerializer,PostAddApiSerializer

from ..models import PostApiModel
from ..utils import check_ordering_kwarg

class PostAPIViewSet(viewsets.ViewSet):
    '''  Viewset to handle GET POST PUT PATCH DELETE requests for
            my Posts API 
             '''
    def list(self, request):
        try:
            limit = int(request.GET.get('limit',None))
        except:
            limit = None
        fields = ['id','title','overview','content',
                  'published_at','author']
        ordering = check_ordering_kwarg(request.GET.get('ordering'),
                                        fields)               
               
        if ordering:
            queryset = PostApiModel.objects.order_by(ordering)
        else:
            queryset = PostApiModel.objects.all()
        serializerd_data = PostApiSerializer(queryset[:limit],many=True)
        return Response(serializerd_data.data)

    def create(self, request):
        last_user = PostApiModel.objects.values('id').last()
        obj_id = last_user.get('id') + 1
        serializerd_data = PostAddApiSerializer(data=request.data)
        if serializerd_data.is_valid():
            return Response({'id':obj_id,**serializerd_data.data})
        return Response(serializerd_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            pk = int(pk)
        except:
            pk = None
        obj = get_object_or_404(PostApiModel,pk=pk)
        serilaizerd_obj = PostApiSerializer(instance=obj)
        return Response(serilaizerd_obj.data)

    def update(self, request, pk=None):
        try:
            pk = int(pk)
        except:
            pk = None
        obj = get_object_or_404(PostApiModel,pk=pk)
        serilaizerd_data = PostAddApiSerializer(instance=obj,data=request.data)
        if serilaizerd_data.is_valid():
            user_id = serilaizerd_data.validated_data.get('user_id').id
            serilaizerd_data.validated_data['user_id'] = user_id
            return Response({'id':obj.id,
                             **serilaizerd_data.validated_data
                             })
        return Response(serilaizerd_data.errors,status=400)

    def partial_update(self, request, pk=None):
        try:
            pk = int(pk)
        except:
            pk = None
        obj = get_object_or_404(PostApiModel,pk=pk)
        serilaizerd_data = PostAddApiSerializer(instance=obj,data=request.data)
        if serilaizerd_data.is_valid():
            user_id = serilaizerd_data.validated_data.get('user_id').id
            serilaizerd_data.validated_data['user_id'] = user_id
            return Response({'id':obj.id,**serilaizerd_data.validated_data})
        return Response(serilaizerd_data.errors,status=400)

    def destroy(self, request, pk=None):
        try:
            pk = int(pk)
        except:
            pk = None
        obj = get_object_or_404(PostApiModel,pk=pk)
        return Response("Post has been deleted")


class PostsSearchAPIView(ListAPIView):
    ''' View for search about users using search filter  '''

    queryset = PostApiModel.objects.all()
    serializer_class = PostApiSerializer
    filter_backends =[filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = ['id','title','overview']
    search_fields = ['id','title','overview','content']

    

class PostsRandomAPIView(ListAPIView):
    queryset = PostApiModel.objects.order_by('?')
    serializer_class = PostApiSerializer
    filter_backends =[filters.OrderingFilter]
    ordering_fields = ['id','title']
    
    def get_queryset(self):
        try:
            limit = int(self.request.GET.get('limit','10'))
        except:
            limit = 10
        return self.queryset[:limit]
