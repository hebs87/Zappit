from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
class PostList(generics.ListAPIView):
    """
    A view to return the Post list
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
