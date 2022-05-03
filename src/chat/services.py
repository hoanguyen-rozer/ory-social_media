from django.conf import settings
from tortoise import Tortoise

from src.chat.tortoise_models import ChatMessage


async def chat_save_message(username, room_id, message, message_type, image_caption):
    """
    Function to store message in database
    """

    await Tortoise.init(**settings.TORTOISE_INIT)
    await Tortoise.generate_schemas()
    await ChatMessage.create(room_id=room_id, username=username, message=message, message_type=message_type,
                             image_caption=image_caption)
    await Tortoise.close_connections()
