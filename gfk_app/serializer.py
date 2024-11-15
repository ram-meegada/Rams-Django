from rest_framework import serializers
from .models import *

class LikesReadSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)
    class Meta:
        model = LikeModel
        fields = ['id', 'users']
