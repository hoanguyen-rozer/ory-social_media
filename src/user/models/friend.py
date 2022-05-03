from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Friend(models.Model):
    """
    Class Friend define relation between inviter and invitee
    """
    inviter = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friends_of_user')
    invitee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_accept = models.BooleanField(_('is accept'), default=False)
    sent_at = models.DateTimeField(_('sent at'), auto_now=True)

    class Meta:
        unique_together = ('inviter', 'invitee')

    def __str__(self):
        return f"{self.inviter.username} send friend request to {self.invitee.username}"
