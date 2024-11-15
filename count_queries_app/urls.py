from django.urls import path
from .views import CountQueriesView, AllBlogsView

urlpatterns = [
    path('count-queries/', CountQueriesView.as_view()),
    
    path('all-blogs/', AllBlogsView.as_view()),
]