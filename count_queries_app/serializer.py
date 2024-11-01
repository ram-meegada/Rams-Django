from rest_framework import serializers
from .models import Comment, BlogPost

class CountQueriesSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text']
    def get_author(self, obj):
        try:
            return obj.author.username
        except Exception as err:
            return str(err)
    def get_post(self, obj):
        try:
            data = {"title": obj.post.title, "content": obj.post.content}
            return data
        except Exception as err:
            return str(err)
