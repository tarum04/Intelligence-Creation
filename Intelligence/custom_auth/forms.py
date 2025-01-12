from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input-box', 'placeholder' : 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-box', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'input-box', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'input-box', 'placeholder': 'Confirm Password'})

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder' : 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder' : 'Password'}))