from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeGroup(models.TextChoices):
    I = 'I', _('individual')
    G = 'G', _('group')


class ChatGroup(Group):
    """ extend Group model to add extra info"""

    type = models.CharField(max_length=1, choices=TypeGroup.choices, default=TypeGroup.I)
    description = models.TextField(blank=True, help_text="description of the group")
    mute_notifications = models.BooleanField(default=False, help_text="disable notification if true")
    icon = models.ImageField(help_text="Group icon", blank=True, upload_to="chartgroup")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('chat:room', args=[str(self.id)])
