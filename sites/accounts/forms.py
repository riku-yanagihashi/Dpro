from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="メールアドレス",
        widget=forms.EmailInput(attrs={
            'class': 'signup-input',
            'placeholder': 'メールアドレスを入力'
        })
    )

    username = forms.CharField(
        required=True,
        label="ユーザー名",
        widget=forms.TextInput(attrs={
            'class': 'signup-input',
            'placeholder': 'ユーザー名を入力'
        }),
        initial=''  # 初期値を空文字に設定
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.icon:
            user.icon = 'icon/default_icon.png'  # デフォルトアイコンのパス
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login-username',
        'placeholder': 'ユーザー名 または メールアドレス'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'login-password',
        'placeholder': 'パスワード'
    }))
