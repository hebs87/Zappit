from django.urls import path, include
from .views import *

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>', PostRetrieveDestroy.as_view()),
    path('posts/<int:pk>/vote', VoteCreate.as_view()),
]
