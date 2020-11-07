from rest_framework import serializers
from django.utils.timesince import timesince 

from ..models import UserApiModel,PostApiModel,CommentApiModel
from ..users_api.serializers import ShortUserApiSerialzer



class PostCommentsSerialzer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    class Meta:
        model = CommentApiModel
        fields = ['name','email','content','created_at']
    
    def get_created_at(self,obj):
        return obj.created_at.strftime('%-d %m, %Y')
    
    def get_timesince(self,obj):
        return timesince(obj.created_at)

class BlogPostApiSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    published_at = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    
    
    class Meta:
        model = PostApiModel
        fields = [
                  'id','author','title','overview',
                  'content','published_at','timesince',
                  'thumbnail'
                  ]
    
    def get_thumbnail(self,obj):
        try:
            url = obj.thumbnail.url
        except:
            url = None
        return url 

    def get_published_at(self,obj):
        return obj.published_at.strftime('%-d %m, %Y')
    
    def get_timesince(self,obj):
        return timesince(obj.published_at)

    def get_author(self,obj):
        return ShortUserApiSerialzer(instance=obj.user_id).data
    
    
class BlogPostDetialApiSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    published_at = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = PostApiModel
        fields = [
                  'id','author','title','overview',
                  'content','published_at','timesince',
                  'thumbnail','comments'
                  ]
    
    def get_thumbnail(self,obj):
        try:
            url = obj.thumbnail.url
        except:
            url = None
        return url 

    def get_published_at(self,obj):
        return obj.published_at.strftime('%-d %m, %Y')
    
    def get_timesince(self,obj):
        return timesince(obj.published_at)

    def get_author(self,obj):
        return ShortUserApiSerialzer(instance=obj.user_id).data
    
    def get_comments(self,obj):
        return PostCommentsSerialzer(obj.comments.all(),many=True).data

