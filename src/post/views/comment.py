from django.http import JsonResponse
from django.views.decorators.http import require_POST

from src.post.forms import CommentAddForm
from src.post.models import Post


@require_POST
def add_comment(request, post_id):
    """
    Create and save new comment data to database
    :return: comment data format json
    """
    post = Post.objects.get(id=post_id)
    comment_form = CommentAddForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
    else:
        return JsonResponse({'success': False, 'message': "Fail to create comment."})
    comment_data = {
        'id': comment.id,
        'content': comment.content,
        'created_at': comment.created_at,
        'user': {
            'id': request.user.id,
            'username': request.user.username,
            'avatar': request.user.avatar.url
        }
    }

    return JsonResponse(comment_data)
