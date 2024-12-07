from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import login, get_backends

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # 必要に応じてcommit=Falseで保存
            if not user.icon:  # デフォルトアイコンを設定（必要なら）
                user.icon = 'path/to/default_icon.png'
            user.save()  # ここでアイコンも含めて保存

            # 認証バックエンドを取得して指定
            backend = get_backends()[0]  # デフォルトのバックエンドを取得
            login(request, user, backend=backend)
            
            return redirect('home')  # サインアップ後のリダイレクト先
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
