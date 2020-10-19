from django.urls import NoReverseMatch
from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.reverse import reverse

from comments.models import Comment

class CommentListSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()



    class Meta:
        model = Comment
        fields = ('user', 'body', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'body', 'created_at', 'updated_at',)


class CommentCreateSerializers(serializers.ModelSerializer):
    user = serializers.CharField(default=serializers.CurrentUserDefault())
    body = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('user', 'body',)


class CommentSerializers(serializers.ModelSerializer):
    body = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('body',)
