from rest_framework import serializers
from django.utils.timesince import timesince 

from ..models import UserApiModel,PostApiModel,CommentApiModel
from ..users_api.serializers import ShortUserApiSerialzer
from ..comments_api.serializers import CommentApiSerializer


class BlogPostApiSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()    
    
    class Meta:
        model = PostApiModel
        fields = [
                  'id','author','title','overview',
                  'content','published_at'
                  ] 


    def get_author(self,obj):
        return ShortUserApiSerialzer(instance=obj.author_id).data
    
    
class BlogPostDetialApiSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    published_at = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = PostApiModel
        fields = [
                  'id','author','title','overview',
                  'content','published_at','timesince'
                  ,'comments'
                  ]

    def get_published_at(self,obj):
        return obj.published_at.strftime('%-d %m, %Y')
    
    def get_timesince(self,obj):
        return timesince(obj.published_at)

    def get_author(self,obj):
        return ShortUserApiSerialzer(instance=obj.author_id).data
    
    def get_comments(self,obj):
        return CommentApiSerializer(obj.comments.all(),many=True).data

