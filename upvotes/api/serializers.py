from rest_framework import serializers

from upvotes.models import Upvote


class UpvoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Upvote
        fields = (
            "user",
            "upvoted_at",
        )
