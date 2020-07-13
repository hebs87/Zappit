from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *


# Create your views here.
class PostList(generics.ListCreateAPIView):
    """
    A view to return the Post list
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Override the standard method to pass in the poster details
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
