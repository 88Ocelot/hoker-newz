from django.contrib.auth import get_user_model
from django.db import models

from posts.models import Post

User = get_user_model()


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='upvotes')
    upvoted_at = models.DateTimeField(auto_now_add=True)
