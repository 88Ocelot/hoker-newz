from rest_framework import viewsets

from comments.mixins import CommentMixin
from hoker_newz.mixins import SerializerClassesMixin
from posts.api import serializers
from posts.models import Post


class PostView(CommentMixin,
               SerializerClassesMixin,
               viewsets.ModelViewSet):
    serializer_classes = {'default': serializers.PostDetailSerializer,
                          'list': serializers.PostListSerializer,
                          'create': serializers.PostCreateSerializer, }
    queryset = Post.objects.all()
