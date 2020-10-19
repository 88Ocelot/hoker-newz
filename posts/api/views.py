from rest_framework import viewsets

from hoker_newz.mixins import SerializerClassesMixin
from posts.api import serializers
from posts.models import Post

class PostView(SerializerClassesMixin,
                viewsets.ModelViewSet):
    serializer_classes = {'default': serializers.PostDetailSerializer,
                          'list': serializers.PostListSerializer,
                          'create': serializers.PostCreateSerializer}
    queryset = Post.objects.all()