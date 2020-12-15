from rest_framework import status

from django.utils import timezone
from django.utils.timesince import timesince
from django.shortcuts import get_object_or_404
from django.conf import settings

from apis.models import CommentApiModel
from apis.global_utils import clean_pk,update_object

from .serializers import CommentAddApiSerializer,CommentApiSerializer
from ..users_api.serializers  import ShortUserApiSerialzer
from ..models import UserApiModel,PostApiModel,CommentApiModel
from ..vars import COMMENTS_CONTENT



import random 

# def json_comment_object(data,created_at=None):
#     if not created_at:
#         created_at = timezone.now()
#     api_user = ShortUserApiSerialzer(data['user_id']).data
#     timesince_ = timesince(created_at)
#     return {
#             'post_id':data['post_id'].id,
#             'user':api_user,
#             'content':data['content'],
#             'create_at':created_at.strftime(settings.DEFAULT_DATETIME_FORMAT),
#             'timesince':timesince_
#             }

def get_new_comment(data,created_at=timezone.now,last_id=1):
    comment_id = random.randint(last_id + 1,100000)
    api_user = ShortUserApiSerialzer(data['user_id']).data
    
    # To get the datetime when this funciton called

    created_at = created_at()
    timesince_ = timesince(created_at)
    return {
            'id':comment_id,
            'post_id':data['post_id'].id,
            'user':api_user,
            'content':data['content'],
            'create_at':created_at.strftime(settings.DEFAULT_DATETIME_FORMAT),
            'timesince':timesince_
            }
    

def get_serialized_data(pk=None,data=None,partial=False):
    pk = clean_pk(pk)
    obj = get_object_or_404(CommentApiModel,pk=pk)
    status_ = status.HTTP_200_OK
    if data:
        serialized_object = CommentAddApiSerializer(obj,data=data,
                                                    partial=partial)
        if serialized_object.is_valid():
            updated_object = update_object(obj,serialized_object.validated_data)
            serialized_data = CommentApiSerializer(updated_object).data
        else:
            serialized_data = serialized_object.errors
            status_ = status.HTTP_400_BAD_REQUEST
    else:
        serialized_data = CommentApiSerializer(instance=obj).data    
    return serialized_data,status_


def create_api_comments(num=0):
    posts = PostApiModel.objects.all()
    for post in posts:
        users = UserApiModel.objects.order_by('?')
        users_num = users.count()
        if users_num < num :
            num = users_num
        
        for user in users[:num]:
            content = random.choice(COMMENTS_CONTENT)
            comment = CommentApiModel.objects.create(post_id=post,
                                                    user_id=user,
                                                    content=content)
                
    return True        