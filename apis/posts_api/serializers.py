from rest_framework import serializers

from django.utils.timesince import timesince
from django.conf import settings

from ..models import PostApiModel
from ..users_api.serializers import ShortUserApiSerialzer


class PostAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = ['title','overview',
                  'content','author_id','published_at']
    

class PostApiSerializer(serializers.ModelSerializer):
    published_at = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = PostApiModel
        fields = ['id','author','title','overview',
                  'content','published_at','timesince']
    
    def get_published_at(self,obj):
        return obj.published_at.strftime(settings.DEFAULT_DATETIME_FORMAT)
    
    def get_author(self,obj):
        return ShortUserApiSerialzer(obj.author_id).data

    def get_timesince(self,obj):
        return timesince(obj.published_at)