from rest_framework import serializers
from django.utils.timesince import timesince 

from ..models import UserApiModel,PostApiModel,CommentApiModel
from ..users_api.serializers import ShortUserApiSerialzer
from ..comments_api.serializers import CommentApiSerializer


class BlogCommentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentApiModel
        fields = ['id','user_id','username','email',
                  'content','created_at']

    
class BlogPostDetialApiSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = PostApiModel
        fields = ['id','author_id','author_name',
                  'author_email','title','overview',
                  'content','published_at','comments']

    
    def get_comments(self,obj):
        return BlogCommentApiSerializer(CommentApiModel.objects.filter(post_id=obj.id),
                                    many=True).data

