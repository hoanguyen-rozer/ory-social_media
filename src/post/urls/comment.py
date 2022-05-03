from django.urls import path

from src.post.views import add_comment

app_name = 'comment'

urlpatterns = [
    path('add/<int:post_id>/', add_comment, name='add_comment'),
]
