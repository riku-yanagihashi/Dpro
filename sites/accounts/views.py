from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.conf import settings

def index(request):
    return render(request, 'accounts/index.html')

class CustomLoginView(LoginView):
    def get_success_url(self):
        # nextパラメータを取得
        redirect_to = self.request.GET.get('next', '')
        # nextが指定されていればそれを返し、なければデフォルトのリダイレクト先
        return redirect_to or resolve_url(self.get_redirect_url()) or super().get_success_url()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # 必要に応じて commit=False で保存
            if not user.icon:  # デフォルトアイコンを設定（必要なら）
                user.icon = 'path/to/default_icon.png'
            user.save()  # ここでアイコンも含めて保存

            # 使用する認証バックエンドを特定
            backend = settings.AUTHENTICATION_BACKENDS[0]  # デフォルトのバックエンドを取得
            
            login(request, user, backend=backend)  # バックエンドのパスを指定してログイン
            
            return redirect('home')  # サインアップ後のリダイレクト先
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
