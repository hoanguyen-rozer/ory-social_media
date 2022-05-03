from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from src.post.models import Feeling, Post, FeelingUser

User = get_user_model()


def express_feeling(request, post_id):
    """
    Allow users express feeling to posts
    :param request:
    :param post_id: ID of the post that the user wants to express feeling.
    :return:
    """
    feeling = Feeling.objects.get(name='like')
    post = Post.objects.get(id=post_id)
    user = request.user
    # expressed_users = [feeling_user.user for feeling_user in post.expressed_users.all()]
    try:
        # Try get FeelingUser object whether have same post and user.
        expressed_by_user = FeelingUser.objects.get(post_id=post_id, user=user)
    except ObjectDoesNotExist:
        FeelingUser.objects.create(post=post, user=user, feeling=feeling)
        return JsonResponse({'success': True, 'message': 'Add feeling successfully'})
    else:
        # FeelingUser object exist, then delete it
        expressed_by_user.delete()
        # if feeling.name == expressed_by_user.feeling.name:
        #     expressed_by_user.delete()
        # else:
        #     expressed_by_user.feeling = feeling
        #     expressed_by_user.save()

        return JsonResponse({'success': True, 'message': 'Update feeling successfully'})

    return JsonResponse({'success': False, 'message': 'Fail to express feeling to the post'})
