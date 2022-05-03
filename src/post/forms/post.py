from django import forms

from src.post.models import Post


class PostCreateForm(forms.ModelForm):
    """
    Create post's content form.
    """
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': "Write something here..."}))

    class Meta:
        model = Post
        fields = ('content', 'checkin')

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control rounded'})


class PostMediaAttachForm(forms.Form):
    """
    Form allow attach media files to post
    """
    media = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(PostMediaAttachForm, self).__init__(*args, **kwargs)
        self.fields['media'].widget.attrs.update({'class': 'custom-file-input d-none'})
