from tortoise import Model, fields


class ChatMessage(Model):
    """
    Use to store chat history message
    """
    id = fields.IntField(pk=True)
    room_id = fields.IntField(null=True)
    username = fields.CharField(max_length=50, null=True)
    message = fields.TextField()
    message_type = fields.CharField(max_length=50, null=True)
    image_caption = fields.CharField(max_length=50, null=True)
    date_created = fields.DatetimeField(null=True, auto_now_add=True)

    class Meta:
        table = 'chat_chatmessage'

    def __str__(self):
        return self.message
