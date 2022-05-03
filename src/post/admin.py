from django.contrib import admin

# Register your models here.
from src.post.models import PostImage, PostTagFriend, FeelingActivity, Post, Feeling, FeelingUser, Comment


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'created_at')


admin.site.register(PostImage)
admin.site.register(PostTagFriend)
admin.site.register(FeelingActivity)
admin.site.register(Feeling)
admin.site.register(FeelingUser)
admin.site.register(Comment)

