from django.urls import path

from src.post.views import express_feeling

app_name = 'feeling'

urlpatterns = [
    path('express/<int:post_id>/', express_feeling, name='express_feeling'),
]
