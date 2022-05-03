from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from tortoise import Tortoise

from .models import ChatGroup
from .tortoise_models import ChatMessage


def get_participants(group_id=None, group_obj=None, username=None):
    """
    Function to get all participants that belong the specific group
    or user in chat box with user who have username argument
    """

    from src.chat.models import TypeGroup
    if group_id:
        chatgroup = ChatGroup.objects.get(id=id)
    else:
        chatgroup = group_obj

    if chatgroup.type == TypeGroup.I:
        user_chat = chatgroup.user_set.exclude(username=username)
        return user_chat[0]
    else:
        temp_participants = []
        for participant in chatgroup.user_set.values_list('username', flat=True):
            if participant != username:
                temp_participants.append(participant.title())
        temp_participants.append('You')
        return ', '.join(temp_participants)


@login_required
def room(request, group_id):
    if request.user.groups.filter(id=group_id).exists():
        chatgroup = ChatGroup.objects.get(id=group_id)
        assigned_groups = list(request.user.groups.values_list('id', flat=True))
        chat_groups = ChatGroup.objects.filter(id__in=assigned_groups)
        groups_participated = [
            {
                'chat_group': chat_group,
                'participants': get_participants(group_obj=chat_group, username=request.user.username)
            }
            for chat_group in chat_groups
        ]
        context = {
            'chatgroup': chatgroup,
            'participants': get_participants(group_obj=chatgroup, username=request.user.username),
            'groups_participated': groups_participated,
        }
        return render(request, 'pages/room.html', context)
    else:
        return HttpResponseRedirect(reverse("chat:unauthorized"))


@login_required
def unauthorized(request):
    return render(request, 'chat/unauthorized.html', {})


async def history(request, room_id):
    await Tortoise.init(**settings.TORTOISE_INIT)
    chat_message = await ChatMessage.filter(room_id=room_id).order_by('date_created').values()
    await Tortoise.close_connections()

    return await sync_to_async(JsonResponse)(chat_message, safe=False)
