# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from src.post.forms import PostCreateForm, PostMediaAttachForm
from src.post.models import PostImage, Post

User = get_user_model()


@require_POST
def post_create_view(request):
    """
    Create and save post data to database.
    :param request:
    :return:
    """
    post_create_form = PostCreateForm(request.POST, prefix='post_create_form')
    post_media_attach_form = PostMediaAttachForm(request.FILES)
    files = request.FILES.getlist('media')
    if post_create_form.is_valid():
        print(post_create_form.cleaned_data)
        post = post_create_form.save(commit=False)
        post.user = request.user
        post.save()
        for file in files:
            post_media = PostImage(media=file)
            post_media.post = post
            post_media.save()
        # post_list = Post.objects.all()
        # context = {
        #     'post_create_form': PostCreateForm(),
        #     'post_media_attach_form': PostMediaAttachForm(),
        #     'post_list': post_list
        # }
        return redirect('page:homepage')
    else:
        print(post_create_form.errors)
        print(post_media_attach_form.errors)
    return HttpResponse("Normal")


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'components/new_feed.html'
    context_object_name = 'post_list'

    def get_queryset(self, **kwargs):
        qs = super(PostListView, self).get_queryset(**kwargs)
        if self.kwargs.get('username', None) is None:
            # print(qs.prefetch_related('user', 'feeling_activity').values())
            return qs.prefetch_related('user', 'feeling_activity')
        else:
            username = self.kwargs.get('username')
            user = User.objects.get(username=username)
            return qs.filter(user=user).prefetch_related('user', 'feeling_activity')


post_list_view = PostListView.as_view()
