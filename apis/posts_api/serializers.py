from rest_framework import serializers

from django.utils.timesince import timesince
from django.conf import settings

from ..models import PostApiModel
from ..users_api.serializers import AuthorApiSerialzer

import datetime

class PostAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = ['title','overview',
                  'content','author_id','published_at']


class PostApiSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = PostApiModel
        fields = ['id','author','title','overview',
                  'content','published_at']
        read_only_fields = ('id',)
    
    def get_author(self,obj):
        return AuthorApiSerialzer(obj.author_id).data

