from django.urls import path

from src.user.views import friend_request_comfirm, friend_request_delete, profile_update

app_name = 'user'

urlpatterns = [
    path('friend/comfirm/<int:friend_request_id>/', friend_request_comfirm, name='friend_request_confirm'),
    path('friend/delete/<int:friend_request_id>/', friend_request_delete, name='friend_request_delete'),
    path('profile_update/process/', profile_update, name='profile_update_process'),
]
