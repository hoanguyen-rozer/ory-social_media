from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.post.models import Post


class Feeling(models.Model):
    name = models.CharField(_('name'), max_length=10)

    def __str__(self):
        return self.name

    def get_icon_src(self):
        """
        Get icon corresponding to feeling
        :return:
        """
        return f"/static/images/icon/{self.name}.png"


class FeelingUser(models.Model):
    """
    Class determine what emotion the user used for the post.
    """
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='expressed_users')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feeling = models.ForeignKey(to=Feeling, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} is feeling {self.feeling.name}"
