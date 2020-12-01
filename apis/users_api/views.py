from rest_framework import viewsets
from rest_framework.authentication import  BasicAuthentication 
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import filters

from django.shortcuts import get_object_or_404

from .serializers import UserApiSerializer
from ..models import UserApiModel
from ..utils import check_ordering_kwarg,update_object,clean_pk
from ..authentication import CsrfExemptSessionAuthentication
                  
from  random import randint



class UserAPIViewSet(viewsets.ViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication,BasicAuthentication)
    '''  Viewset to handle GET POST PUT PATCH DELETE requests for
            my Users API 
             '''
    def list(self, request):
        limit = get_limit(request.GET)
        fields = ['id','first_name','last_name','full_name',
                  'username','gender','birthday','birth_place',
                  'email','phone_number','address',]
        ordering = check_ordering_kwarg(request.GET.get('ordering'),
                                        fields)               
               
        if ordering:
            queryset = UserApiModel.objects.order_by(ordering)
        else:
            queryset = UserApiModel.objects.all()
        serializerd_data = UserApiSerializer(queryset[:limit],many=True)
        return Response(serializerd_data.data)

    def create(self, request):
        last_user = UserApiModel.objects.values('id').last()
        obj_id = randint(last_user.get('id') + 1,100000)
        serializerd_data = UserApiSerializer(data=request.data)
        if serializerd_data.is_valid():
            return Response({'id':obj_id,**serializerd_data.data})
        return Response(serializerd_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(UserApiModel,pk=pk)
        serilaizerd_obj = UserApiSerializer(instance=obj)
        return Response(serilaizerd_obj.data)

    def update(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(UserApiModel,pk=pk)
        serilaizerd_data = UserApiSerializer(instance=obj,data=request.data)
        if serilaizerd_data.is_valid():
            updated_obj = update_object(obj,serilaizerd_data.validated_data)        
            return Response(UserApiSerializer(instance=updated_obj).data)
        return Response(serilaizerd_data.errors,status=400)

    def partial_update(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(UserApiModel,pk=pk)
        serilaizerd_data = UserApiSerializer(instance=obj,data=request.data,partial=True)
        if serilaizerd_data.is_valid(): 
            updated_obj = update_object(obj,serilaizerd_data.validated_data)        
            return Response(UserApiSerializer(instance=updated_obj).data)
        return Response(serilaizerd_data.errors,status=400)

    def destroy(self, request, pk=None):
        pk = clean_pk(pk)
        obj = get_object_or_404(UserApiModel,pk=pk)
        return Response("User has been deleted")


class UsersSearchAPIView(ListAPIView):
    ''' View for search about users using search filter  '''

    queryset = UserApiModel.objects.all()
    serializer_class = UserApiSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ['id','username', 'email','full_name','birth_place',
                     'phone_number','address','birthday']
    

class UsersRandomAPIView(ListAPIView):
    queryset = UserApiModel.objects.order_by('?')
    serializer_class = UserApiSerializer
    
    def get_queryset(self):
        limit = get_limit(request.GET,10)
        return self.queryset[:limit]

