from rest_framework import serializers

from comments.models import Comment


class CommentListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user', 'body', 'created_at', 'updated_at',)
        read_only_fields =('user', 'body', 'created_at', 'updated_at',)