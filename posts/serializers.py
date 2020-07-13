from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    """
    A serializer to convert the Post model to JSON
    """
    # Enables us to automatically set the user when post is created - poster value is set in the view
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'poster_id', 'created', 'votes']

    # Get the number of votes for a particular post
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class VoteSerializer(serializers.ModelSerializer):
    """
    A serializer to convert the Post model to JSON
    """
    class Meta:
        model = Vote
        fields = ['id']
