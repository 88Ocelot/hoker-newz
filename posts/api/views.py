from rest_framework import viewsets,permissions

from comments.mixins import CommentMixin
from hoker_newz.mixins import SerializerClassesMixin, PermissionClassesMixin
from hoker_newz.permissions import IsOwner
from posts.api import serializers
from posts.models import Post
from upvotes.mixins import UpvoteMixin


class PostView(CommentMixin,
               UpvoteMixin,
               SerializerClassesMixin,
               PermissionClassesMixin,
               viewsets.ModelViewSet):
    permission_classes = {
        'create': (permissions.IsAuthenticated,),
        'list': (permissions.AllowAny,),
        'update': (IsOwner,),
        'default': (permissions.IsAuthenticated,),
        'retrieve': (permissions.AllowAny,),
        'comments_list': (permissions.AllowAny,),

    }

    serializer_classes = {'default': serializers.PostDetailSerializer,
                          'list': serializers.PostListSerializer,
                          'create': serializers.PostCreateSerializer,
                          'update': serializers.PostUpdateSerializer,}
    queryset = Post.objects.all()
