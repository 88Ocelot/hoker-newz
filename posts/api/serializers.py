from rest_framework import serializers

from posts.models import Post


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = serializers.HyperlinkedIdentityField(view_name='posts-comments-list', read_only=True)
    upvotes = serializers.HyperlinkedIdentityField(view_name='posts-upvote-list', read_only=True)
    upvote_url = serializers.HyperlinkedIdentityField(view_name='posts-upvote', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'comments', 'upvotes', 'upvote_url', 'created_at', 'updated_at',)


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body',)


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(view_name='posts-detail')

    class Meta:
        model = Post
        fields = ('title', 'body', 'author', 'created_at', 'get_upvotes', 'url')


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(default=serializers.CurrentUserDefault())



    class Meta:
        model = Post
        fields = ('title', 'body', 'author',)
