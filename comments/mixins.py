from rest_framework import decorators, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from comments.api.serializers import (
    CommentCreateSerializers,
    CommentListSerializers,
    CommentSerializers,
)
from comments.models import Comment


class CommentMixin:
    """
    Mixin for adding comment function to viewset
    """

    comments_serializers = {
        "comment": CommentCreateSerializers,
        "comments_list": CommentListSerializers,
        "comment_update": CommentSerializers,
        "comment_detail": CommentSerializers,
    }

    @decorators.action(
        url_path="comment",
        detail="comment-create",
        methods=("POST",),
    )
    def comment(self, request, pk):
        print(request.user)
        serializer = self.get_serializer_class()(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            comment = Comment.objects.create(**serializer.validated_data, post_id=pk)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.action(
        url_path="comments",
        detail="comments-list",
        methods=("GET",),
    )
    def comments_list(self, request, pk):
        comments = Comment.objects.filter(post_id=pk)
        serializer = self.get_serializer_class()(
            comments, many=True, context={"request": request}
        )
        return Response(serializer.data)

    @decorators.action(
        url_path="comments/(?P<comment_id>\d+)",
        detail="comment-update",
        methods=(
            "PUT",
            "PATCH"
        ),
    )
    def comment_update(self, request, pk, comment_id):
        queryset = Comment.objects.all()
        obj = get_object_or_404(queryset, id=comment_id, post=pk)
        serializer = self.get_serializer_class()(obj, data=request.data, partial=True)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
    @decorators.action(
        url_path="comments/(?P<comment_id>\d+)",
        detail="comment-detail",
        methods=( "GET",),
    )
    def comment_detail(self, request, pk, comment_id):
        queryset = Comment.objects.all()
        obj = get_object_or_404(queryset, id=comment_id, post=pk)

        serializer = self.get_serializer_class()(obj, context={'request': request,
                                                               'comment_id':comment_id,
                                                               'pk':pk})
        return Response(serializer.data)



    def get_serializer_class(self):
        if self.action not in self.comments_serializers.keys():
            return super(CommentMixin, self).get_serializer_class()
        else:
            return self.comments_serializers.get(self.action)
