from django_filters import rest_framework as filters

from posts.models import Post


class PostFilterSet(filters.FilterSet):
    created_range = filters.RangeFilter(field_name="created_at")

    class Meta:
        model = Post
        fields = ("created_range",)
