from rest_framework import serializers

from ..models import PostApiModel



class PostAddApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = ['title','overview',
                  'content','user_id','published_at']
    

class PostApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = ['id','title','overview',
                  'content','user_id','published_at']
    