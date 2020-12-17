from rest_framework import serializers

from django.utils.timesince import timesince
from django.conf import settings

from ..models import CommentApiModel
from ..users_api.serializers import ShortUserApiSerialzer

class CommentApiSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = CommentApiModel
        fields = ['id','post_id','content','created_at']
        read_only_fields = ('id',)
    
    def get_created_at(self,obj):
        return obj.created_at.strftime(settings.DEFAULT_DATETIME_FORMAT)
    
    

class CommentAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentApiModel
        fields = ['id','user_id','post_id','content']
        read_only_fields = ('id',)
        