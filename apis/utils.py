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
    try:
        limit = int(request.GET.get('limit',None))
    except:
        limit = initial
    return limit

def check_ordering_kwarg(order,fields):
    try:
        order = order.strip()
    except:
        return None
    if order:
        if order in fields:
            return order
        elif '-' == order[0]:
            if order[1:].strip() in fields:
                return  '-{}'.format(order[1:].strip())  
    return None

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_thumnail_name(title,image_name):
    slug_title = slugify(title)
    imgName,imgExt = os.path.splitext(image_name)
    random_str = random_string_generator(size=6)
    img_name = slug_title + '-' + random_str + imgExt
    img_path = os.path.join('posts_thumbnails',img_name)
    return img_path


def update_object(obj,data):
        for attr, value in data.items():
            setattr(obj, attr, value)
        return obj