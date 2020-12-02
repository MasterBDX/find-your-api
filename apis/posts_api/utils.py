from django.utils.timesince import timesince
from django.utils.timezone import now
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status

from .serializers import PostApiSerializer,PostAddApiSerializer


from ..global_utils import (update_object)
from ..models import PostApiModel

from random import randint

def get_new_post(data):
    '''
       Get new post object without saving it using passed data   
    '''
    last_post = PostApiModel.objects.values('id').last()
    id_ = randint(last_post.get('id') + 1,100000)
    obj = PostApiModel(id=id_,
                       title=data['title'],
                       overview=data['overview'],
                       content=data['content'],
                       author_id=data['author_id'],
                       published_at=data.get('published_at',now()))
    return obj


def get_serialized_data(pk,data=None,partial=False):
    '''Get Serialized Data For 
       Retrieve and Update and 
       Partial Update methods'''
       
    status_ = status.HTTP_200_OK
    obj = get_object_or_404(PostApiModel,pk=pk)
    if data:
        serilaized_obj = PostAddApiSerializer(instance=obj,
                                            data=data,
                                            partial=partial)
        if serilaized_obj.is_valid():
            updated_object = update_object(obj,serilaized_obj.validated_data)
            data = PostApiSerializer(updated_object).data
        else:
            data = serilaized_obj.errors
            status_ = status.HTTP_400_BAD_REQUEST
    else:
        serilaized_obj = PostApiSerializer(instance=obj)
        data = serilaized_obj.data        
    return data,status_