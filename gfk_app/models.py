from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    text = models.TextField()

class LikeModel(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='contentType')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    users = models.ManyToManyField(User, related_name="liked_users")
