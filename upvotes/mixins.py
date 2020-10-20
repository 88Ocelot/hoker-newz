from rest_framework import decorators, status
from rest_framework.response import Response

from upvotes.api.serializers import UpvoteSerializer
from upvotes.models import Upvote


class UpvoteMixin:
    """
    Mixin for adding like function to viewset
    """

    upvote_serializers = {
        "upvote_list": UpvoteSerializer,
        "upvote": UpvoteSerializer,
    }

    @decorators.action(
        url_path="upvote",
        detail="upvote",
        methods=("POST",),
    )
    def upvote(self, request, pk):
        upvote = Upvote.objects.filter(user=request.user.id, post_id=pk)
        if upvote.exists():
            upvote.delete()
            return Response("like removed")
        else:
            Upvote.objects.create(post_id=pk, user=request.user)
            return Response("like added")
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @decorators.action(
        url_path="upvotes",
        detail="upvote-list",
        methods=("GET",),
    )
    def upvote_list(self, request, pk):
        upvotes = Upvote.objects.filter(post_id=pk)
        serializer = self.get_serializer_class()(
            upvotes, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action not in self.upvote_serializers.keys():
            return super(UpvoteMixin, self).get_serializer_class()
        else:
            return self.upvote_serializers.get(self.action)
