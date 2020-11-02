from rest_framework import serializers

from ..models import PostApiModel


class PostApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApiModel
        fields = [...]
    