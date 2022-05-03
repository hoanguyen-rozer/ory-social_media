from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model

from src.user.models import Friend

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'email', 'is_active')


@admin.register(Friend)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'inviter', 'invitee', 'sent_at', 'is_accept')
