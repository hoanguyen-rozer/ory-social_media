from django.urls import path

from . import views
from ..page.views import chat_page_view

app_name = 'chat'

urlpatterns = [
    path('', chat_page_view, name='chat_page'),
    path('history/<str:room_id>/', views.history, name='history'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('<str:group_id>/', views.room, name='room'),
]
