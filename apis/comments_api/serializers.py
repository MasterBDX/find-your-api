from rest_framework import serializers

from django.utils.timesince import timesince
from django.conf import settings

from ..models import CommentApiModel
from ..users_api.serializers import ShortUserApiSerialzer

class CommentApiSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    post_title = serializers.SerializerMethodField()

    class Meta:
        model = CommentApiModel
        fields = ['id','post_id','post_title','username',
                  'content','created_at','timesince']
        read_only_fields = ('id',)

    def get_timesince(self,obj):
        return timesince(obj.created_at)
    
    def get_created_at(self,obj):
        return obj.created_at.strftime(settings.DEFAULT_DATETIME_FORMAT)
    
    def get_username(self,obj):
        return obj.user.username
    
    def get_post_title(self,obj):
        return obj.post_id.title


class CommentAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentApiModel
        fields = ['id','user_id','post_id','content']
        read_only_fields = ('id',)
        