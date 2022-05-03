from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from src.user.models.friend import Friend


class Gender(models.TextChoices):
    MALE = 'm', _('Male')
    FEMALE = 'f', _('Female')
    OTHER = 'o', _('Other')


class MaritalStatus(models.TextChoices):
    SINGLE = 'single', _('Single')
    MARRIED = 'married', _('Married')
    WIDOWED = 'widowed', _('Widowed')
    DIVORCED = 'divorced', _('Divorced')
    SEPARATED = 'separated', _('Separated')


class User(AbstractUser):
    """
    Custom class user
    """
    city = models.CharField(_('city'), max_length=50, blank=True, null=True)
    gender = models.CharField(_('gender'), max_length=1, choices=Gender.choices, blank=True, null=True)
    dob = models.DateField(_('date of birth'), blank=True, null=True)
    marital_status = models.CharField(_('marital status'), max_length=15, choices=MaritalStatus.choices, blank=True,
                                      null=True)
    contact_number = models.CharField(_('contact number'), max_length=15, blank=True, null=True)

    avatar = models.ImageField(_('avatar'), upload_to='user/avatar/', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    @property
    def full_name(self):
        """
        Get fullname of user
        """
        return f"{self.first_name} {self.last_name}"

    def get_avatar(self):
        """
        Get avatar of user.
        If user have not set their avatar, return default static avatar.
        """
        self.defaul_avatar = '/static/images/user.png'
        if self.avatar:
            return self.avatar.url
        return self.defaul_avatar

    def get_friend_request(self):
        """
        Get list friend requests of user.
        """
        return Friend.objects.filter(is_accept=False, invitee=self)

    def get_friend_list(self):
        """
        Get list friend objects of user.
        Include accepted requests where the user is the invitee or invitee.
        :return: [Friend]
        """
        return Friend.objects.filter(Q(is_accept=True, inviter=self) | Q(is_accept=True, invitee=self))

    def get_friend_list_of_user(self):
        """
        Get list user objects which are friends of user.
        :return: [User]
        """
        friend_of_user = self.get_friend_list()
        friend_list = [friend.invitee if friend.invitee != self else friend.inviter for friend in friend_of_user]
        return friend_list

    def get_friend_quantity(self):
        """
        Get number of friends of user
        :return:
        """
        friend_list = self.get_friend_list()
        return friend_list.count()
