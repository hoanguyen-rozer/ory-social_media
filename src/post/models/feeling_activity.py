from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeFA(models.TextChoices):
    FEELING = ('F', 'feeling')
    ACTIVITY = ('A', 'activity')


class FeelingActivity(models.Model):
    type = models.CharField(_('type'), choices=TypeFA.choices, max_length=1)
    name = models.CharField(_('name'), max_length=15)
    status_description = models.CharField(_('status description'), max_length=50)

    class Meta:
        verbose_name = 'feeling/activity'
        verbose_name_plural = 'feeling/activities'

    def __str__(self):
        return f"{self.type} {self.name}"
