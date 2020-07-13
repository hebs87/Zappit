from django.urls import path, include
from .views import *

urlpatterns = [
    path('posts/', PostList.as_view()),
]
