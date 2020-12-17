from rest_framework import serializers

from django.utils.timesince import timesince
from django.conf import settings

from ..models import CommentApiModel
from ..users_api.serializers import ShortUserApiSerialzer

class CommentApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentApiModel
        fields = ['id','user_id','username','email',
                  'post_id','content','created_at']
        read_only_fields = ('id',)

class CommentAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentApiModel
        fields = ['id','user_id','post_id',
                  'username','email','content']
        read_only_fields = ('id',)
        