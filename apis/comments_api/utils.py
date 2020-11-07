from django.utils import timezone
from django.utils.timesince import timesince
from django.shortcuts import get_object_or_404
from django.conf import settings

from ..users_api.serializers  import ShortUserApiSerialzer
from ..models import UserApiModel


def json_comment_object(data,created_at=None):
    if not created_at:
        created_at = timezone.now()
    api_user = ShortUserApiSerialzer(data['user_id']).data
    timesince_ = timesince(created_at)
    return {
            'post_id':data['post_id'].id,
            'user':api_user,
            'content':data['content'],
            'create_at':created_at.strftime(settings.DEFAULT_DATETIME_FORMAT),
            'timesince':timesince_
            }