from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from src.user.forms import ProfileUpdateForm
from src.user.models import Friend

User = get_user_model()


@require_POST
def friend_request_comfirm(request, friend_request_id):
    """
    Accept friend request
    :param request:
    :param friend_request_id:
    :return:
    """
    friend_request = Friend.objects.get(id=friend_request_id)
    friend_request.is_accept = True
    friend_request.save()
    return JsonResponse(request, {'success': True, 'message': 'Confirm friend request successfully'})


@require_POST
def friend_request_delete(request, friend_request_id):
    """
    Cancel friend request
    :param request:
    :param friend_request_id:
    :return:
    """
    friend_request = Friend.objects.get(id=friend_request_id)
    friend_request.delete()
    return JsonResponse(request, {'success': True, 'message': 'Cancel friend request successfully'})


class ProfileUpdateView(TemplateView, LoginRequiredMixin):
    template_name = 'pages/profile_update.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        username = self.request.user
        user_info = User.objects.get(username=username)
        profile_update_form = ProfileUpdateForm(instance=user_info)
        context.update({
            'profile_update_form': profile_update_form,
        })
        return context


profile_update_view = ProfileUpdateView.as_view()


@require_POST
def profile_update(request):
    """
    Save updated data user to db
    :param request:
    :return:
    """
    user = request.user
    profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
    if profile_update_form.is_valid():
        profile_update_form.save()
        return redirect(reverse('page:profile_update'))
    else:
        print('ERROR: ', profile_update_form.errors)
        # return HttpResponse('error')
        return render(request, 'pages/profile_update.html', {'profile_update_form': profile_update_form})
