from django import forms

from src.post.models import Comment


class CommentAddForm(forms.ModelForm):
    """
    Form allow user comment on the post.
    """

    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super(CommentAddForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control rounded'})
