from django.utils.timesince import timesince
from django.utils.timezone import now
from django.utils.text import Truncator
from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status

from .serializers import PostApiSerializer,PostAddApiSerializer


from ..global_utils import (update_object)
from ..models import PostApiModel,UserApiModel

from apis.vars import POSTS_CONTENTS,POSTS_TITLES

from itertools import count
from datetime import timedelta,date
from random import randint,choice
import os

def get_new_post(data,last_id=1):
    '''
       Get new post object without saving it using passed data   
    '''
    id_ = randint(last_id + 1,100000)
    data.setdefault('published_at',now())
    data['id'] = id_
    obj = PostApiModel(**data)
    
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

def create_api_posts(num=0):
    users = UserApiModel.objects.all()
    counter = count(1)
    today = date.today()
    time_delta = timedelta(days=1)
    for user in users:
        for time in range(num):
            key = choice(list(POSTS_CONTENTS.keys()))
            post_title = str(counter.__next__()) + ' ' + POSTS_TITLES.get(key,'Title')
            post_content = POSTS_CONTENTS.get(key,'Content')
            overview = Truncator(post_content).words(12,truncate='...')
        
            obj = PostApiModel.objects.create(
                                        author_id=user,
                                        title=post_title,
                                        overview=overview,
                                        content=post_content,
                                        published_at=today,
                                        )
            today -= time_delta
    print('done')       
    return True