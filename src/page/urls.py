from django.urls import path

from src.page.views import homepage_view, profile_page_view, privacy_setting_page_view
from src.user.views import profile_update_view

app_name = 'page'

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('profile/<str:username>/', profile_page_view, name='profile_page'),
    path('profile_update/', profile_update_view, name='profile_update'),
    path('privacy_setting/', privacy_setting_page_view, name='privacy_setting_page'),
]
