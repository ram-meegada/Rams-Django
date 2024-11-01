from django.urls import path
from .views import CountQueriesView

urlpatterns = [
    path('count-queries/', CountQueriesView.as_view())
]