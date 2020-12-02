import random
import string
import os
from django.utils.text import slugify


def clean_pk(pk):
    '''this function checks whether pk is an integer'''
    try:
        pk = int(pk)
    except:
        pk = None
    return pk

def get_limit(data,initial=None):
    ''' Check if limit kwarg from request.GET is an int'''
    try:
        limit = int(data.get('limit',None))
    except:
        limit = initial
    return limit

def check_ordering_kwarg(kwarg,fields):
    ''' Check if kwarg is in existing fields 
        and have no empty spaces '''
    try:
        kwarg = kwarg.strip()
    except:
        return None
    if kwarg:
        if kwarg in fields:
            return kwarg
        elif '-' == kwarg[0]:
            if kwarg[1:].strip() in fields:
                return  '-{}'.format(kwarg[1:].strip())  
    return None

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_thumnail_name(title,image_name):
    ''' Rename posts thumbnails with new format '''

    slug_title = slugify(title)
    imgName,imgExt = os.path.splitext(image_name)
    random_str = random_string_generator(size=6)
    img_name = slug_title + '-' + random_str + imgExt
    img_path = os.path.join('posts_thumbnails',img_name)
    return img_path


def update_object(obj,data):
    '''To update object attrs with out saving it in datatbase'''
    for attr, value in data.items():
        setattr(obj, attr, value)
    return obj