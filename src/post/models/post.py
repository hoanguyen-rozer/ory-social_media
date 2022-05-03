from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.post.models import feeling_activity


class Post(models.Model):
    content = models.TextField(_('content'))
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_of_user')
    feeling_activity = models.ForeignKey(to=feeling_activity.FeelingActivity, on_delete=models.SET_NULL, null=True,
                                         blank=True)
    checkin = models.CharField(_('checkin'), max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.user.username} - {self.content}"

    def get_expressed_users(self):
        """
        Get user objects expressed emotion in this post
        """
        feeling_user_with_post = self.expressed_users.all()
        expressed_users = [feeling_user.user for feeling_user in feeling_user_with_post]
        return expressed_users


class PostImage(models.Model):
    """
    Class allow multiple media in one post.
    """
    media = models.FileField(_('media'), upload_to='post/media/')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='images_of_post')


class PostTagFriend(models.Model):
    """
    Class determine who users are tagged in the post
    """
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='tag_friend_of_post')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts_is_tagged')
