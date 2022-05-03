# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from src.chat.models import ChatGroup
from src.chat.views import get_participants
from src.post.forms import PostCreateForm, PostMediaAttachForm
from src.post.models import Post

User = get_user_model()


class HomepageView(LoginRequiredMixin, TemplateView):
    """
    Class Homepage TemplateView
    """
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        post_create_form = PostCreateForm(prefix='post_create_form')
        post_media_attach_form = PostMediaAttachForm()
        post_list = Post.objects.prefetch_related('user', 'feeling_activity')
        context.update({
            'post_create_form': post_create_form,
            'post_media_attach_form': post_media_attach_form,
            'post_list': post_list
        })
        return context


homepage_view = HomepageView.as_view()


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfilePageView, self).get_context_data(**kwargs)
        username = kwargs.get('username')
        user = User.objects.get(username=username)
        post_list = Post.objects.filter(user=user).prefetch_related('user', 'feeling_activity')
        context.update({
            'user_profile': user,
            'friend_list': user.get_friend_list_of_user(),
            'post_list': post_list
        })
        return context


profile_page_view = ProfilePageView.as_view()


class ChatPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/chat.html'

    def get_context_data(self, **kwargs):
        context = super(ChatPageView, self).get_context_data(**kwargs)

        # Get groups which user is assigned
        assigned_groups = list(self.request.user.groups.values_list('id', flat=True))
        chat_groups = ChatGroup.objects.filter(id__in=assigned_groups)

        groups_participated = [
            {
                'chat_group': chat_group,
                'participants': get_participants(group_obj=chat_group, username=self.request.user.username)
            }
            for chat_group in chat_groups
        ]
        context.update({
            'groups_participated': groups_participated,
        })
        return context


chat_page_view = ChatPageView.as_view()


class PrivacySettingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/privacy_setting.html'


privacy_setting_page_view = PrivacySettingPageView.as_view()
