from django.urls import path

from src.post.views import post_create_view, post_list_view

app_name = 'post'

urlpatterns = [
    path('create/', post_create_view, name='create'),
    path('list/', post_list_view, name='list'),
    path('list/<str:username>/', post_list_view, name='list_by_user'),
]
