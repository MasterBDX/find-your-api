from ..users_api.serializers import ShortUserApiSerialzer

from django.utils.timesince import timesince
from django.conf import settings
from django.utils import timezone

def json_post_object(data):
    author = ShortUserApiSerialzer(data['author_id']).data
    published_at = data.get('published_at')
    if not published_at:
        published_at = timezone.now()
       
    return {
            'author':author,
            'title':data['title'],
            'overview':data['overview'],
            'content':data['content'],
            'published_at':published_at.strftime(settings.DEFAULT_DATETIME_FORMAT),
            'timesince':timesince(published_at)
            }