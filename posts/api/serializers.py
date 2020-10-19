from rest_framework import serializers

from posts.models import Post
from upvotes.api.serializers import UpvoteSerializer



class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    upvotes = UpvoteSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('title', 'body','author', 'upvotes')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'get_upvotes')


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'created_at', 'get_upvotes',)


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('title', 'body', 'author',)
