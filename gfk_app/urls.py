from django.urls import path
from .views import *

urlpatterns = [
    path('posts/<int:post_id>/like/', IncrementPostLikesView.as_view()),
]
