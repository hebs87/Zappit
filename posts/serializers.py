from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    """
    A serializer to convert the Post model to JSON
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'created']
