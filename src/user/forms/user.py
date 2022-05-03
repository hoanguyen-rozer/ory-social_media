from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.contrib.auth import get_user_model

from src.user.models.user import Gender

User = get_user_model()


class LoginForm(LoginForm):
    """
    Inherit class LoginForm of allauth package and add class stylesheet to this class's fields.
    """

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control mb-0'})
        self.fields['password'].widget.attrs.update({'class': 'form-control mb-0'})
        self.fields['remember'].widget.attrs.update({'class': 'custom-control-input'})


class SignupForm(SignupForm):
    """
    Inherit class SignupForm of allauth package and add class stylesheet to this class's fields.
    """

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-0'})
        self.fields['username'].widget.attrs.update({'class': 'form-control mb-0'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control mb-0'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control mb-0'})


class ProfileUpdateForm(forms.ModelForm):
    """
    Model form is used to user update personal information.
    """
    gender = forms.ChoiceField(choices=Gender.choices,
                               widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}), required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = User
        fields = ('avatar', 'first_name', 'last_name', 'city', 'gender', 'dob', 'marital_status')

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'class': 'file-upload'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'disabled': True, 'required': False})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['dob'].widget.attrs.update({'class': 'form-control'})
        self.fields['marital_status'].widget.attrs.update({'class': 'form-control'})
