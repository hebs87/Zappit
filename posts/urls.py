from django.urls import path, include
from .views import *

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', VoteCreate.as_view()),
]
