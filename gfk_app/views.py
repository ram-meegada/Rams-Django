from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import F
from rest_framework.response import Response
from .models import *
from django.contrib.contenttypes.models import ContentType
from .serializer import *

class IncrementPostLikesView(APIView):
    def post(self, request, post_id):
        try:
            content_type = ContentType.objects.get_for_model(PostModel)
            post = PostModel.objects.get(id=post_id)
            like_obj, created = LikeModel.objects.get_or_create(
                content_type=content_type,
                object_id=post.id
            )
            like_obj.users.add(request.data["user_id"])
            like_obj.save()
            return Response({'data': None, 'message': 'Post liked successfully', 'status': 200})
        except Exception as err:
            return Response({'data': str(err), 'message': 'Something went wrong', 'status': 400})

    def get(self, request, post_id):
        # try:
            content_type = ContentType.objects.get_for_model(PostModel)
            post = PostModel.objects.get(id=1000)
            like_objs = LikeModel.objects.filter(
                content_type=content_type,
                object_id=post.id
            ).prefetch_related('users')
            serializer = LikesReadSerializer(like_objs, many=True)
            return Response({'data': serializer.data, 'message': 'Count of likes fetched ', 'status': 200})
        # except Exception as err:
        #     return Response({'data': str(err), 'message': 'Something went wrong', 'status': 400})
