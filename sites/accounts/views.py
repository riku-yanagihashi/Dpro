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
            user = form.save(commit=False)
            if not user.icon:  # デフォルトアイコンの設定
                user.icon = 'path/to/default_icon.png'
            user.save()  # 保存

            # backendを文字列で指定
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('home')  # サインアップ後のリダイレクト先
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
