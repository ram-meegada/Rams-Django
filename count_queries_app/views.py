from django.shortcuts import render
from django.db import connection, reset_queries

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BlogPost, Comment
from .serializer import *


class CountQueriesView(APIView):
    def get(self, request):
        reset_queries()
        all_comments = Comment.objects.select_related('author', 'post')
        serializer = CountQueriesSerializer(all_comments, many=True)
        data = serializer.data
        queries_count = len(connection.queries)
        return Response({'data': data, 'queries_count': queries_count, 'message': 'All comments fetched successfully', 'status': 200})

class AllBlogsView(APIView):
    def get(self, request):
        reset_queries()
        all_blogs = BlogPost.objects.prefetch_related('comment_set')
        serializer = BlogsReadSerializer(all_blogs, many=True)
        data = serializer.data
        queries_count = len(connection.queries)
        return Response({'data': data, 'queries_count': queries_count, 'message': 'All blogs fetched successfully', 'status': 200})
