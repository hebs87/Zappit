from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

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


class VoteCreate(generics.CreateAPIView):
    """
    A view to return the Post list
    """
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        voter = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=voter, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post :)')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
