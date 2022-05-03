from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.post.models import Post


class Comment(models.Model):
    """
    Class determine what user commented on the post.
    """
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments_on_post')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_by_user')
    content = models.CharField(_('content'), max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"
