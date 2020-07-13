from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import *
from .serializers import *


# Create your views here.
class PostList(generics.ListCreateAPIView):
    """
    A view to return the Post list and allow post creation
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Override the standard method to pass in the poster details
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    """
    A view to allow users to vote/remove vote
    DestroyModelMixin allows us to delete records
    """
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Check if user has voted on a particular post
    def get_queryset(self):
        voter = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=voter, post=post)

    # Check if user has voted on a particular post before saving vote
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post :)')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

    # Check if user has voted on a particular post before deleting vote
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise ValidationError('You never voted for this post!')
