from django.utils.timesince import timesince
from ..models import PostApiModel
from django.utils.timezone import now

from random import randint

def get_post_object(data):
    '''Get  post object without saving it 
        using passed data   
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