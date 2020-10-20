from rest_framework import serializers

from comments.models import Comment


class CommentLinkField(serializers.HyperlinkedIdentityField):
    def get_url(self, obj, view_name, request, format):

        if hasattr(obj, 'pk') and obj.pk in (None, ''):
            return None
        if hasattr(obj, 'id') and obj.pk in (None, ''):
            return None
        kwargs = {
            'pk': getattr(obj,'pk'),
            'comment_id': getattr(obj,'id')
        }
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)


class CommentListSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    url = CommentLinkField(view_name='posts-comment-detail',
                           read_only=True)

    class Meta:
        model = Comment
        fields = (
            "user",
            "body",
            "created_at",
            "updated_at",
            'url',
        )
        read_only_fields = (
            "user",
            "body",
            "created_at",
            "updated_at",
        )


class CommentCreateSerializers(serializers.ModelSerializer):
    user = serializers.CharField(default=serializers.CurrentUserDefault())
    body = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = (
            "user",
            "body",
        )


class CommentSerializers(serializers.ModelSerializer):
    body = serializers.CharField(required=True)

    class Meta:
        model = Comment
        fields = ("body",)
