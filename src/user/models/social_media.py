from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Social(models.Model):
    name = models.CharField(_('name'), max_length=50)


class SocialMedia(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='social_media_of_user')
    social = models.ForeignKey(to=Social, on_delete=models.CASCADE)
    url = models.URLField(_('social url'))
    updated_at = models.DateTimeField(auto_now=True)
