from rest_framework import serializers

from django.utils.timesince import timesince
from django.conf import settings

from ..models import PostApiModel
from ..users_api.serializers import AuthorApiSerialzer

import datetime

class PostAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = ['title','overview','author_id',
                  'author_name','author_email',
                  'content','published_at']


class PostApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = ['id','author_id','author_name',
                  'author_email','title','overview',
                  'content','published_at']
        read_only_fields = ('id',)

